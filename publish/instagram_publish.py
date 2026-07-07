#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Publica um post (carrossel ou imagem única) no Instagram via Instagram Graph API.

Uso:
    python instagram_publish.py <pasta_do_post> [--dry-run]

A pasta do post deve conter as artes numeradas 01.png, 02.png, ... (na ordem de
publicação) e um README.md com a seção "## Legenda" (usada como caption).
`foto-capa.png` e outros arquivos não-numerados são ignorados.

Requer variáveis de ambiente (no GitHub Actions, via Secrets):
    IG_USER_ID       -> ID da conta do Instagram (Instagram Business Account ID)
    IG_ACCESS_TOKEN  -> token de longa duração com instagram_content_publish

Hospedagem das imagens (a Meta busca a imagem por URL pública):
    - Se RAW_BASE estiver definido (repo público), monta a URL raw do GitHub:
        RAW_BASE = https://raw.githubusercontent.com/<owner>/<repo>/<branch>
      e a imagem vira  {RAW_BASE}/<caminho-relativo-no-repo>
    - Caso contrário, faz upload temporário para um host público (0x0.st / catbox).
"""
import os, sys, time, glob, re, json
import requests

GRAPH = "https://graph.facebook.com/v21.0"
IG_USER_ID = os.environ.get("IG_USER_ID", "")
TOKEN = os.environ.get("IG_ACCESS_TOKEN", "")
RAW_BASE = os.environ.get("RAW_BASE", "").rstrip("/")
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def log(*a): print(*a, flush=True)


def caption_from_readme(folder):
    p = os.path.join(folder, "README.md")
    if not os.path.exists(p):
        return ""
    txt = open(p, encoding="utf-8").read()
    m = re.search(r"##\s*Legenda\s*\n(.+?)(?:\n##\s|\n>\s|\Z)", txt, re.S)
    if not m:
        return ""
    return m.group(1).strip()


def slides(folder):
    fs = sorted(glob.glob(os.path.join(folder, "[0-9][0-9].png")))
    if not fs:
        raise SystemExit(f"Nenhuma arte NN.png encontrada em {folder}")
    return fs


def public_url(path):
    """Devolve uma URL pública para a imagem local."""
    if RAW_BASE:
        rel = os.path.relpath(path, REPO_ROOT).replace(os.sep, "/")
        return f"{RAW_BASE}/{rel}"
    # upload temporário (repo privado)
    for host in ("https://0x0.st", "https://catbox.moe/user/api.php"):
        try:
            with open(path, "rb") as f:
                if "catbox" in host:
                    r = requests.post(host, data={"reqtype": "fileupload"},
                                      files={"fileToUpload": f}, timeout=60)
                else:
                    r = requests.post(host, files={"file": f}, timeout=60)
            if r.ok and r.text.strip().startswith("http"):
                return r.text.strip()
        except Exception as e:
            log(f"  upload falhou em {host}: {e}")
    raise SystemExit(f"Não consegui hospedar a imagem: {path}")


def gpost(path, **params):
    params["access_token"] = TOKEN
    r = requests.post(f"{GRAPH}/{path}", data=params, timeout=120)
    d = r.json()
    if "error" in d:
        raise SystemExit(f"Erro Graph API: {json.dumps(d['error'], ensure_ascii=False)}")
    return d


def wait_ready(container_id, tries=20):
    for _ in range(tries):
        r = requests.get(f"{GRAPH}/{container_id}",
                         params={"fields": "status_code", "access_token": TOKEN}, timeout=30)
        st = r.json().get("status_code")
        if st == "FINISHED":
            return True
        if st == "ERROR":
            raise SystemExit(f"Container {container_id} deu ERROR")
        time.sleep(3)
    return False


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    folder = os.path.abspath(sys.argv[1])
    dry = "--dry-run" in sys.argv
    imgs = slides(folder)
    caption = caption_from_readme(folder)
    log(f"Post: {folder}")
    log(f"Slides: {len(imgs)} | Caption: {len(caption)} chars")

    urls = [public_url(p) for p in imgs]
    for u in urls: log("  img:", u)
    if dry:
        log("DRY-RUN: não publicado."); return
    if not (IG_USER_ID and TOKEN):
        raise SystemExit("Defina IG_USER_ID e IG_ACCESS_TOKEN.")

    if len(urls) == 1:
        c = gpost(f"{IG_USER_ID}/media", image_url=urls[0], caption=caption)
        wait_ready(c["id"])
        pub = gpost(f"{IG_USER_ID}/media_publish", creation_id=c["id"])
        log("PUBLICADO (imagem única):", pub.get("id")); return

    # carrossel (2 a 10 itens)
    if not (2 <= len(urls) <= 10):
        raise SystemExit(f"Instagram aceita 2 a 10 itens no carrossel (tem {len(urls)}).")
    children = []
    for u in urls:
        ch = gpost(f"{IG_USER_ID}/media", image_url=u, is_carousel_item="true")
        children.append(ch["id"])
    parent = gpost(f"{IG_USER_ID}/media", media_type="CAROUSEL",
                   children=",".join(children), caption=caption)
    if not wait_ready(parent["id"]):
        raise SystemExit("Container do carrossel não ficou pronto a tempo.")
    pub = gpost(f"{IG_USER_ID}/media_publish", creation_id=parent["id"])
    log("PUBLICADO (carrossel):", pub.get("id"))


if __name__ == "__main__":
    main()
