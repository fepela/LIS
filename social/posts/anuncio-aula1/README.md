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

## Zonas de segurança (Reels / Stories)

Layout reposicionado em 05/09/2026 depois que o preço apareceu na faixa coberta pela UI.

| Elemento | Posição | Observação |
|---|---|---|
| Topo 0–14% (0–269px) | **vazio** | barra de UI do Reels |
| Logo | y 196 | abaixo da barra superior |
| Kicker + chamada | y 290–576 | |
| **Faixa de vídeo** | **y 604–1212** (1080×608) | material 16:9 sem corte |
| **Preço** | **y 1240–1490** | logo abaixo do vídeo |
| Base 21% (1517–1920px) | **vazio** | legenda, áudio e CTA do Meta |
| Coluna direita 8% | **vazia** | botões de ação |

A linha de apoio *"Método completo de IA aplicada, do zero ao avançado"* **saiu da arte** — era
ela que empurrava o preço para a zona coberta. Esse texto vai no campo de texto do anúncio,
que é onde o Meta já o exibe.

---

> Arte em **Poppins** (stand-in) — arte final oficial em **Google Sans**.
> `poster.png` = frame para thumb/prévia.
