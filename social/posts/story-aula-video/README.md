# Stories em vídeo — Aula "Agente de Social com o Claude Code" (2 opções)

Composição do **vídeo do Felipe** (`social/referencia/VIDEO NOSSO.mp4`, 9:16, ~10,7s,
com áudio) com o layout da aula da Comunidade ChapterIA. **Sem Higgsfield** —
feito 100% local (Playwright para o overlay + ffmpeg para a composição).

**Formato:** 1080×1920 (9:16) · ~10,7s · H.264 · **com áudio** · paleta ChapterIA.

## Versão final
- ⭐ **`opcao-A-animada.mp4`** — **VERSÃO FINAL (texto animado).** Base da opção A
  full-bleed, com os textos entrando em **fade + slide escalonado** enquanto o
  Felipe fala: badge (0,4s) → kicker (1,2s) → headline (1,7s) → selo (3,1s) →
  CTA (4,2s). Áudio original mantido.

## Opções anteriores (referência)
- ✅ **`opcao-A-fullbleed.mp4`** — opção A com textos fixos (base da versão final).
  (preview: `preview-A.png`)
- **`opcao-B-card.mp4`** — vídeo num **card arredondado** em cima, sobre fundo de
  marca (petróleo + grid), textos embaixo. Mais **“designed”/promocional** e
  separa bem vídeo × texto. (preview: `preview-B.png`)

Ambas: logo + badge **▶ NOVA AULA** + **≈ 1 HORA**; kicker COMUNIDADE CHAPTERIA;
headline com **Claude Code** em ciano; selo **🔒 Conteúdo exclusivo da Comunidade
ChapterIA**; CTA **Faça parte · link na bio**.

## Como publicar
- Sobe como **Stories** (ou Reels). O áudio original do Felipe é mantido.
- Em Stories, usar o **sticker de link** apontando pra Comunidade (o botão
  "Faça parte" é visual).

## Observações
- Nada de warp de texto: os textos são vetoriais, sobrepostos por cima do vídeo.
- O overlay é regenerável em `build_vidov.py` (troca de textos/posições) e a
  composição em ffmpeg (ver histórico da sessão).

---

> Arte em **Poppins** (stand-in) — arte final oficial em **Google Sans**.
