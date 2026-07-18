# Reel/Stories animado — Teaser "IA aplicada" (ChapterIA)

Post **animado** (vídeo) de marca, no sistema premium dark da ChapterIA. Hub com
vida (glow pulsando, partículas, leve push-in) + revelação dos textos + CTA.

**Arquivo:** `reel-teaser.mp4`
**Formato:** 1080×1920 (9:16) · 8s · 24fps · H.264 · mudo
**Poster:** `poster.png` (frame final, pode ser a capa/thumb).
**Paleta:** ChapterIA — petróleo + ciano. Fonte Poppins (stand-in da Google Sans).

## Roteiro (8s)
- 0–1,5s: hub surge e ganha vida (glow pulsando, partículas subindo).
- 1,7s: entra **"A IA parou de só responder."**
- 3,2s: entra **"Agora ela trabalha com você."** (trabalha com você em ciano).
- 5,2s: entra o CTA **@chapteria · Aprenda IA aplicada · link na bio**.
- Push-in sutil ao longo de todo o vídeo.

## Como foi feito (100% local, sem dependência externa)
- Animação vetorial (HTML/CSS/SVG) com engine `setFrame(t)` determinística.
- 192 frames renderizados via Playwright/Chromium → montados em H.264 com ffmpeg.
- **Sem warp de texto** (texto entra nítido, não é IA de vídeo).
- Teste de motion por IA (Higgsfield/Kling) validado à parte; pode ser incorporado
  depois como camada de fundo via editor, se desejado.

## Como publicar
- Sobe como **Reels** ou **Stories**. Sugestão: adicionar uma trilha (música)
  no editor do Instagram — o vídeo é mudo de propósito.
- Em Stories, usar o **sticker de link** (o "link na bio" do vídeo é visual).

## Retematizar (fácil)
O texto é trocável no `build_anim.py` (linhas `l1`, `l2`, chip e CTA). Dá pra
gerar versões: oferta dos 7 capítulos, ChatGPT Work, Claude, etc. — só mudar as
strings e re-renderizar.

---

> Arte em **Poppins** (stand-in) — arte final oficial em **Google Sans**.
