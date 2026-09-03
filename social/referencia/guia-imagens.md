# Guia de busca e uso de imagem — ChapterIA

> Complementa `guia-social.md`. Vale para toda peça: carrossel, reel, capa, story.
> Em conflito com este documento, `CLAUDE.md` vence.

## A regra que resolve 90% dos casos

**Busque o conceito, nunca o nome próprio.**

Buscar o título de um filme, o nome de uma marca ou de uma pessoa produz um de dois
resultados, e os dois são ruins:

1. **Vem outra coisa.** Buscamos `maverick` no Unsplash: voltaram quatro carros — o Ford
   Maverick. Um deles descrito como *"Traditional Brasilian Muscle car Ford Maverick"*.
   Nenhum still de filme.
2. **Vem a coisa certa, e aí é pior.** Se aparecer foto de pôster, marquise de cinema ou
   captura de tela, a licença do banco **não cobre a obra retratada dentro da foto**. O
   fotógrafo licenciou a fotografia dele; não licenciou o filme que está no enquadramento.

Em vez do nome, busque **o mecanismo**: o que a matéria está de fato explicando.

| Pauta | ❌ Busca ruim | ✅ Busca boa |
|---|---|---|
| Clonagem de voz no Brutalista | `the brutalist` | `recording studio microphone` |
| Voz do Val Kilmer em Maverick | `top gun maverick` | `microphone black background` |
| Dublagem brasileira | `dublagem` | `dubbing studio headphones` |
| Interstícios do Late Night | `late night with the devil` | `vintage television` |
| Netflix e IA | `netflix` | `movie theater seats` |

## Como buscar bem

1. **Um conceito por busca.** A própria ferramenta avisa: lista de palavras-chave composta não
   melhora resultado. Cinco conceitos = cinco buscas.
2. **Trave a direção de arte nos filtros.** `orientation` e `color` são o que fazem nove fotos
   de nove fotógrafos diferentes lerem como uma peça só. Para a nossa paleta:
   `orientation: portrait` + `color: black` funciona bem.
3. **Leia `description` e `alt_description` antes de baixar.** É lá que aparece o que está de
   fato no quadro — e onde alguns autores pedem crédito específico.
4. **Olhe a imagem.** Texto alternativo erra. Baixar e ver custa dez segundos e evita publicar
   com um logo de terceiro no canto.
5. **Existe `search_illustrations` e `search_collections`**, além de `search_photos`. Coleção
   costuma render um conjunto mais coerente que buscas soltas.

## O que rejeitar sempre

- **Rosto identificável**, em qualquer peça que possa ser impulsionada. A licença do Unsplash
  permite uso comercial, mas **não dá direito sobre pessoas ou marcas que apareçam na foto**.
- **Logo, marca, escudo, uniforme de time, pôster, tela de produto de terceiro.**
- **Foto que retrata obra protegida** — pôster, still, capa de disco, arte em exposição.
- Qualquer coisa que precise de uma frase explicando por que é seguro. Se precisa explicar,
  não é.

Prefira **objeto e ambiente**: microfone, projetor, poltrona, fone, mesa de som, TV antiga.
Não têm titular de direito de imagem e atravessam qualquer revisão de anúncio.

## Quando nenhuma foto serve

Para o que é protegido — still de filme, tela de produto, interface de concorrente — o caminho
é **recriar**, não buscar:

- **Recriação em CSS**, marcada como `tela ilustrativa · recriação` ou
  `representação esquemática — não é captura do filme`. Já usamos em telas de ChatGPT, Gemini,
  Claude, Lovable, YouTube e num site fictício de cliente.
- **Cartela esquemática**, que mostra o *mecanismo* em vez da cena. Costuma informar mais que a
  imagem original: quarenta modelos treinados com um aceso diz o que um still de avião não diz.
- **Press kit oficial**, baixado pelo cliente, quando o still for realmente necessário. Quase
  sempre vem com termo *editorial only* — ou seja, **não impulsionar**.

## Tratamento, para tudo virar uma peça só

Foto entra como **fundo**, nunca como conteúdo. Aplicar:

- `grayscale(.42) contrast(1.06) brightness(.92)` na imagem;
- camada de tinta petróleo com brilho ciano no topo;
- crédito do fotógrafo na borda direita, na vertical.

O crédito não é exigido pela licença do Unsplash — é cortesia com quem fotografou, e custa nada.

## Nomes com caracteres fora do latino

A Poppins não tem glifos CJK, cirílicos ou árabes: o nome vira tofu na arte. Use o **nome de
usuário** do fotógrafo nesses casos (`cshong / Unsplash` em vez dos caracteres originais).

---

> Registrado em 03/09/2026, depois da busca por `maverick` que devolveu carros.
