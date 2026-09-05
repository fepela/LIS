# Anúncios — ChapterIA

Criativos de tráfego pago. Um por aula, mais um guarda-chuva.

| Pasta | Chamada | Duração |
|---|---|---|
| `aula1` | Crie seu primeiro **Agente de IA** na prática | 46s |
| `aula2` | Transforme uma ideia em um **SaaS** com IA | 42s |
| `aula3` | Um **agente** que atende e vende por você | 31s |
| `aula4` | Torne-se um **profissional Super IA** | 37s |
| `aula5` | Monte um **sistema de conteúdo** com IA | 68s |
| `aula6` | Crie seu **influencer digital** com IA | 68s |
| `aula7` | Crie **sites e apresentações** com IA | 22s |
| `geral` | Aprenda IA aplicada, do **zero ao avançado** | 104s |

## O formato

**1080×1920 · 30fps · H.264 · áudio original copiado sem reencode.**

O material de origem é 16:9 e entra numa **faixa de 1080×608 em y=600**, sem corte — o
enquadramento original é preservado inteiro. Acima, logo + kicker + chamada. Abaixo, a oferta.

**Sem botão e sem "link na bio":** o CTA é inserido pela própria plataforma de anúncios.

## A oferta na arte

> de ~~R$ 99,90~~ por **R$ 49,90**
> em até **9x de R$ 6,71** · ou à vista no Pix

**Sem período no preço** — não há "/mês" nem "/ano". O acesso por 12 meses fica para a página
de vendas.

## Zonas de segurança

Todo o conteúdo vive entre **y 295 e 1486**, dentro dos limites 269–1517. Os 14% superiores,
os 21% inferiores e a coluna de 8% à direita ficam vazios.

O gerador (`build_ad.py`, no diretório de trabalho) desenha as guias por cima quando se
adiciona a classe `guides` ao body — é assim que a geometria é conferida antes de compor.

## Pendências

- **Duração.** Cinco das oito passam de 40s; o Meta costuma performar melhor entre 15 e 30s.
  Só a `aula7` (22s) está nessa faixa. Cortes curtos exigem escolher o trecho de cada aula.
- **O preço riscado.** "De R$ 99,90" só passa na revisão de anúncios se for preço real
  praticado. Se for âncora que nunca foi cobrada, convém remover.

---

> Fonte dos vídeos: `social/referencia/Aula1.mp4`…`Aula7.mp4` e `geral.mp4`.
> Tipografia **Poppins** (stand-in) — arte final oficial em **Google Sans**.
> `poster.png` = quadro para thumb e prévia.
