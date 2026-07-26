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
- **Faixa inferior:** linha de apoio *Do zero ao avançado, com método.* + CTA
  **Quero começar · link na bio** + **@chapteria**.
- Texto entra com **fade-in** suave no início; CTA visível o anúncio inteiro.

## Observações
- **Copy do anúncio é facilmente editável** (`build_ad.py`): hook, kicker, CTA.
  Variações possíveis (mais direto, com preço/oferta, com prova social, etc.).
- Para Meta Ads, versões mais curtas (15–30s) tendem a performar melhor — dá
  pra cortar um trecho do material e regerar mantendo o mesmo frame de marca.
- Respeita safe zones (texto recuado da direita; CTA acima do rodapé).

---

> Arte em **Poppins** (stand-in) — arte final oficial em **Google Sans**.
> `poster.png` = frame para thumb/prévia.
