# Oferta "7 capítulos + bônus" — estáticos

Peças de imagem da assinatura ChapterIA, com a **oferta nova**. Vieram de
`social/posts/feed-oferta-7-capitulos` e `social/posts/story-oferta-7-capitulos`
e foram trazidas pra cá porque agora rodam como anúncio.

| Arquivo | Formato | Uso |
|---|---|---|
| `01.png` → `04.png` | 1080×1080 (2160² @2x) | carrossel de feed, nessa ordem |
| `feed-unico.png` | 1080×1080 (2160² @2x) | post estático avulso |
| `story.png` | 1080×1920 (2160×3840 @2x) | Stories |

## A oferta na arte

> de ~~R$ 99,90~~ por **R$ 49,90**
> em até **9x de R$ 6,71** — ou à vista no Pix

**Sem período no preço.** Saiu o "/mês" da headline e do bloco de preço, e saiu o
"R$ 297/ano — melhor custo-benefício" que ancorava a versão anterior. O acesso por
12 meses fica para a página de vendas.

## Zonas de segurança

Só o `story.png` tem zona de segurança a respeitar (9:16). Todo o conteúdo vive entre
**y 306 e 1493**, dentro dos limites 269–1517, e a borda direita para em **x 984**,
antes da coluna de 8% dos botões de ação. Medido no DOM, não no olho.

Para caber nessa faixa a lista perdeu as descrições de cada capítulo — ficaram só os
títulos, numerados. A leitura melhorou; a descrição completa continua no carrossel
(`02.png` e `03.png`) e na legenda.

Os quadrados não precisam disso: no feed a arte aparece inteira.

## Estrutura do carrossel

1. **01.png** — capa: "Por R$ 49,90 você aprende a construir:" + subtítulo + "arraste →".
2. **02.png** — capítulos 1–4.
3. **03.png** — capítulos 5–7 + ★ Bônus · Campanha no Meta Ads.
4. **04.png** — preço, botão **Comece agora**, *link na bio*, "+ encontros semanais
   ao vivo e comunidade".

`feed-unico.png` condensa tudo num quadrado só, sem a lista: headline
"Aprenda IA na prática e comece a construir." + o que o método cobre + preço + CTA.

## Como publicar

- **Carrossel:** `01→04.png` na ordem.
- **Post único:** `feed-unico.png` sozinho.
- **Stories:** `story.png` + **sticker de link** apontando pra página de assinatura —
  o botão "Comece agora" é visual.
- **Como anúncio:** o CTA vem da plataforma; o botão desenhado vira redundante mas
  não atrapalha.

## Pendências

- **O preço riscado.** "De R$ 99,90" só passa na revisão do Meta se for preço real
  já praticado. Se for âncora que nunca foi cobrada, convém remover.

## Legenda sugerida

Por R$ 49,90 você não assiste aula: você constrói. 🔷

No método completo da ChapterIA você sai com 7 aplicações reais de IA funcionando — do seu primeiro agente no WhatsApp a um SaaS no ar:

• Agente de IA no WhatsApp — seu primeiro agente funcional
• SaaS com IA — sua ideia virando produto
• Atendimento e Vendas — um agente que vende por você
• Profissional Super IA — produtividade de verdade
• Social Media com IA — conteúdo que não trava
• Influencer Digital — vídeos e personagens com IA
• Sites e Apresentações — prontos em minutos
★ Bônus · Campanha no Meta Ads

+ encontros semanais ao vivo e comunidade.

De R$ 99,90 por R$ 49,90, em até 9x de R$ 6,71 ou à vista no Pix. Link na bio pra começar. 👆

#IA #InteligenciaArtificial #ChapterIA #AgentesDeIA #SaaS #Produtividade

---

> Tipografia **Poppins** (stand-in) — arte final oficial em **Google Sans**.
> Geradores no diretório de trabalho: `oferta_sq_1..4.html`, `oferta_unico.html`
> (quadrados) e `build_story.py` (9:16, que reaproveita as fontes e o logo dos quadrados).
