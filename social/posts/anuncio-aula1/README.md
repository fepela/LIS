# Anúncio (Reels) — Aula 1 · "Crie seu primeiro Agente de IA"

Primeiro **anúncio** da ChapterIA. O material de origem
(`social/referencia/Aula1.mp4`) é **landscape 16:9 (~46s)** e foi transformado em
**Reels 9:16** com a identidade visual da marca. **Sem Higgsfield** — Playwright
(frame de marca) + ffmpeg (composição).

**Formato:** 1080×1920 (9:16) · ~46s · 30fps · H.264 · **áudio original
preservado (`-c:a copy`, não editado).**

## Layout (landscape → vertical)
- Vídeo original enquadrado numa **faixa central** (1080×608), sem cortar
  conteúdo, com fio ciano nas bordas.
- **Faixa superior (marca):** logo + kicker **CHAPTERIA · AULA 1** + hook
  **"Crie seu primeiro Agente de IA na prática."**
- **Faixa inferior:** linha de apoio *Método completo de IA aplicada, do zero ao
  avançado.* + **preço em destaque: de ~~R$ 99,90~~ por R$ 49,90**.
- **Sem botão / sem "link na bio"** — o CTA é inserido pela própria plataforma de
  anúncios (Meta Ads). Texto entra com **fade-in** suave no início.

## Observações
- **Copy do anúncio é facilmente editável** (`build_ad.py`): hook, kicker, preço.
  Variações possíveis (mais direto, com preço/oferta, com prova social, etc.).
- Para Meta Ads, versões mais curtas (15–30s) tendem a performar melhor — dá
  pra cortar um trecho do material e regerar mantendo o mesmo frame de marca.
- Respeita safe zones (texto recuado da direita; CTA acima do rodapé).

## Oferta na arte (atualizada em 05/09/2026)

Faixa inferior traz **de ~~R$ 99,90~~ por R$ 49,90**, com a linha
*em até 9x de R$ 6,71 · ou à vista no Pix*.

**Sem período no preço** — não há "/mês" nem "/ano". A oferta inclui acesso por 12 meses,
mas isso fica para a página de vendas, não para a arte.

**Sem botão e sem "link na bio"** — o CTA é inserido pela própria plataforma de anúncios.

---

> Arte em **Poppins** (stand-in) — arte final oficial em **Google Sans**.
> `poster.png` = frame para thumb/prévia.
