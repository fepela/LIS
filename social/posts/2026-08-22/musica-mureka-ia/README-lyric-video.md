# Lyric Video — "Próximo Capítulo" (música feita com Mureka.ai)

**Entrega:** `lyric-video-completo.mp4` · 9:16 · **3:45 (225s)** · 30fps · **COM ÁUDIO** (a faixa inteira).
**Áudio:** `social/referencia/musica.MP3` (versão final da faixa).
**Produção:** 100% local (HTML/CSS/JS → captura quadro a quadro → ffmpeg). **Custo: 0 créditos.**

> Duração passa do limite de Reel (~90s). Este corte é para **YouTube, comunidade e Stories em série**.
> Para Reel, use `reel-musica-mureka.mp4` (20s) que já está nesta pasta.

## O que mudou em relação à versão de 20s

A versão curta era um videoclipe: b-roll + waveform + player. Esta é um **lyric video**: a letra
aparece **sincronizada com o canto**, e cada bloco da música ganha uma **cena gráfica da marca**
que brinca com o que está sendo dito. Os clipes de `/tocando/` deixaram de ser o fundo o tempo
todo e passaram a entrar **pontualmente**, nos momentos de mais energia.

## Como a sincronia foi feita

A marcação de tempo veio **do cliente**, bloco a bloco (a cada 10–12s da faixa). Dentro de
cada bloco os versos são distribuídos por **peso silábico** — verso longo ocupa mais tempo —
com um teto por verso para que os gritos curtos não estiquem. Quando o teto deixa uma sobra,
ela vira respiro instrumental em vez de texto parado na tela.

A faixa tem **30 segundos de introdução instrumental** antes do primeiro verso. Esse trecho
ganhou uma abertura própria: lockup da marca, depois duas cartelas explicando o que é a peça,
e um convite pra subir o som — tudo sobre o b-roll respirando.

> **Nota de versão:** a primeira montagem usou `0822.MP3` (3:27) e a sincronia foi estimada por
> análise espectral (FFT + detecção de andamento), já que não há transcritor de áudio neste
> ambiente. Com a faixa final (`musica.MP3`, 3:45) e os tempos informados pelo cliente, essa
> estimativa foi substituída pela marcação real.

### Ajuste fino da letra

O arquivo **`letra.lrc`** traz cada verso com seu tempo. É um `.lrc` padrão — abre em qualquer
editor de texto. Se algum verso entrar adiantado ou atrasado, corrija o tempo (`[mm:ss.cc]`) e
me devolva o arquivo: eu re-renderizo com a sua marcação exata.

## Roteiro de cenas

| Trecho | Cena |
|---|---|
| **0–30s** · abertura | Lockup `chapterIA` + cartelas de contexto sobre o b-roll |
| **Verso 1** | Letra em karaokê (rolagem) + janela de terminal em "uma máquina do seu lado" |
| | Chips **criar · construir · transformar** acendendo em sequência |
| **Pré-refrão** | Verso solo, grande e centralizado — quebra de ritmo |
| **Refrão** | **b-roll revelado**, "ChapterIA!" em ciano gigante pulsando no nível do áudio |
| **Verso 2** | Chips **agentes · negócios · automações · conteúdo · produtos** |
| | **Gráfico dos 7 capítulos** — sete barras preenchendo em "São sete capítulos na prática" |
| **Pré-refrão 2** | Contraste **✕ promessa** / **✓ projeto de pé** |
| **respiros** | Sobras entre blocos — b-roll quase limpo, só waveform |
| **Ponte** | Tom mais baixo, alternativas fantasma ("um freela", "uma nova profissão"...) |
| **Refrão final** | Energia máxima, tudo ligado |
| **Final** | Cartelas curtas + lockup da marca + "começa agora" |

## Elementos permanentes

- **Waveform reativa de verdade:** 48 bandas log-espaçadas (40–9000 Hz) extraídas por FFT
  quadro a quadro do MP3, com ataque/liberação suavizados. Ela responde à música, não é loop.
- **Barra de progresso** da faixa, chip **MÚSICA FEITA COM IA · MUREKA.AI**, logo + `@chapteria`.
- **Motion** conforme `emilkowalski-motion`: só `transform`/`opacity`, uma linguagem de easing,
  entradas curtas, sem loop decorativo.

## Legenda sugerida

A gente compôs uma música pra apresentar o projeto — e transformou ela num lyric video. 🎸🔷 (com som!)

A faixa saiu do Mureka.ai. O clipe saiu daqui: a letra sincronizada, as cenas, a waveform que reage ao espectro real do áudio — tudo montado localmente, quadro a quadro.

E tem um detalhe técnico que vale mais que a música: não usei nenhum transcritor pra sincronizar a letra. Extraí a energia da faixa por FFT, achei as viradas de seção pelos degraus de volume, detectei o andamento (~129 BPM) e encaixei cada verso na grade de compassos, distribuindo por peso silábico.

Por que isso importa pra você? Porque é mais uma rota de renda: **trilha sob encomenda + lyric video**. Todo cliente que lança algo precisa de música e de um vídeo pra ela. Faixa de banco genérico é o detalhe que denuncia produção barata.

Salva pra fazer o seu. 👇

#IA #Musica #Mureka #LyricVideo #RendaExtra #ChapterIA

---

> Música e letra: ChapterIA (composição feita no Mureka.ai; faixa final `musica.MP3`).
> B-roll: assets do cliente em
> `social/referencia/tocando/` (visual gerado por IA). Tipografia **Poppins** (stand-in).
> Paleta oficial: petróleo `#1A334A` · paraquedista `#18A3B7` · ciano `#27E6EC`.
