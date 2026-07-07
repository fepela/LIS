# Conteúdos de pauta (notícias de IA) — fundo branco

Linha de conteúdo reativa às notícias de IA. Regra que rege (de [`../../CLAUDE.md`](../../CLAUDE.md)):
**notícia só entra com aplicação prática** — cada peça responde "como isso ajuda
quem acompanha a ChapterIA?". Sem sensacionalismo; rumores enquadrados como
"segundo reportagem". Direção visual: **fundo branco**, logo colorido, texto
Azul Petróleo, destaques em Paraquedista/Ciano (marca-texto). Render em Poppins
(arte final: Google Sans).

Assets em [`assets/pauta/`](assets/pauta/).


## Integração de geração de imagem (Google Imagen 4)
- Imagens realistas agora são **geradas direto no ambiente** via API do Google
  (Imagen 4), a única acessível pela política de rede. Requer billing ativo.
- Gerador reutilizável (fora do repo): `scratchpad/genimg.py` (prompts em json).
- **Sempre rotular as artes como "Imagem ilustrativa · IA"** — a foto NÃO é da
  agência; a fonte da *notícia* (Reuters/Guardian) vai só na legenda.
- Capas do Lote 2 geradas: `assets/pauta/lote2-gerado/` (`L2-*.png` originais,
  `capa-0X.png` compostas).

## Direção visual (atualizada)
- **Fundo branco limpo**, sem gradiente atrás do logo.
- **Foto realista por assunto** no topo (layout foto-ready). Exemplo de layout:
  `assets/pauta/demos-foto-ready/exemplo-cover-foto-ready.png`.
- As fotos são **geradas pelo Felipe** (como no carrossel #02) e compostas aqui.

### Briefing de imagens (prompts prontos)
Estilo comum (usar em todas, para coesão): *fotografia realista, luz natural
suave, paleta com azuis frios discretos, clima limpo e moderno, sem texto
legível, sem logotipos de terceiros, proporção 4:3.*

- **#1 Claude/trabalho:** escritório moderno minimalista; laptop com uma interface
  de agente de IA executando tarefas/fluxo; clima executivo, detalhes em azul.
- **#8 Caso da cachorra:** cena acolhedora em casa, luz quente; pessoa no sofá com
  um cachorro ao lado, segurando celular/notebook; emoção de cuidado.
- **#10 Delegar:** flat lay de mesa de trabalho; mãos digitando, monitor com uma
  automação rodando sozinha, café e caderno; minimalista, tons neutros.
- **#2 Governo EUA:** prédio institucional/mesa de reunião séria com uma tela de
  dados/IA ao fundo; tom sóbrio, azul-acinzentado.
- **#3 OpenAI infraestrutura:** data center / servidores com bandeira dos EUA
  desfocada ao fundo; escala e importância nacional.
- **#4 ChatGPT superapp:** smartphone com vários apps/ícones convergindo em um só;
  ideia de central de trabalho; limpo, moderno.
- **#5 Manus x China/Meta:** tabuleiro de xadrez ou mapa-múndi com peças de tech;
  metáfora de disputa geopolítica; sóbrio.
- **#6 Manus recompra:** linha do tempo/handshake corporativo desfeito e refeito;
  clima de negociação.
- **#7 Perplexity Comet:** navegador moderno numa tela respondendo em vez de listar
  links; foco em busca conversacional.
- **#9 DeepMind/ética:** pessoa pensativa (filósofo) diante de uma tela com rede
  neural sutil; clima reflexivo, luz suave.

## Status das 10 pautas

| # | Tema | Formato | Status |
|---|---|---|---|
| 1 | Claude Sonnet 5 (colega de trabalho) | Carrossel análise (6) | ✅ produzido |
| 2 | Anthropic + governo EUA | Carrossel explicativo | ⬜ copy pronto abaixo |
| 3 | OpenAI como infraestrutura (5% ao governo) | Reels provocativo | ⬜ |
| 4 | ChatGPT vira "superapp" | Carrossel/Reels | ⬜ |
| 5 | Manus x Meta x China | Reels de contexto | ⬜ |
| 6 | Manus pode voltar aos investidores | Carrossel linha do tempo | ⬜ |
| 7 | Perplexity Comet (futuro da busca) | Reels explicativo | ⬜ |
| 8 | Caso: tutor + ChatGPT + cachorra | Carrossel storytelling (7) | ✅ produzido |
| 9 | DeepMind + ética (filósofo) | Carrossel denso | ⬜ |
| 10 | Chatbots → agentes ("delegar") | Estático manifesto | ✅ produzido |

> Nas pautas 3, 4, 5, 6 os fatos são **reportagens/rumores** — comunicar sempre
> com "segundo reportagem/Reuters", sem afirmar como fato consumado.

---

## ✅ #10 — Estático manifesto "perguntar → delegar"
Arte: `assets/pauta/10-delegar-estatico.png`.
> **Legenda:**
> Tem uma mudança silenciosa acontecendo na IA: ela parou de só *responder* e
> começou a *executar*.
>
> A geração nova de modelos navega, planeja, programa e entrega tarefas inteiras.
> A habilidade que vale ouro deixou de ser "escrever o prompt perfeito" e virou
> "saber o que delegar".
>
> Comece simples: pense em 1 tarefa repetitiva, de passos claros, que consome seu
> tempo. É por aí que a IA vira produtividade de verdade.
>
> Salve e siga a @chapteria. 👉
> #InteligenciaArtificial #IA #Produtividade #Agentes #ChapterIA

## ✅ #1 — Carrossel "Claude Sonnet 5"
Artes: `assets/pauta/01-claude-sonnet5-01..06.png`.
> **Legenda:**
> A Anthropic lançou o Claude Sonnet 5, com foco em tarefas agênticas — navegar,
> planejar, programar e executar. Traduzindo: a IA está saindo do "chatbot que
> responde" para o "agente que faz".
>
> Isso muda o jogo pra você: o valor não está mais em fazer 10 perguntas, e sim
> em delegar uma tarefa bem definida e acompanhar o resultado.
>
> Quer aprender a fazer isso na prática? Segue a @chapteria. 🔗 Link na bio.
> #Claude #Anthropic #InteligenciaArtificial #Agentes #ChapterIA

## ✅ #8 — Carrossel storytelling "caso da cachorra"
Artes: `assets/pauta/08-caso-cachorra-01..07.png`.
> **Legenda:**
> Um tutor recebeu o pior diagnóstico sobre a cachorra dele, a Rosie: câncer. Em
> vez de parar, ele usou IA (como o ChatGPT) — junto de cientistas e com
> supervisão veterinária — para apoiar a pesquisa de uma vacina personalizada.
>
> O ponto não é "a IA curou". É que uma pessoa comum conseguiu pesquisar,
> organizar hipóteses e fazer perguntas melhores para quem entende.
>
> Essa é a IA que ensinamos aqui: copiloto de raciocínio, com critério. Ela apoia
> a decisão — não substitui o profissional.
>
> Segue a @chapteria pra usar IA assim. 💙
> #InteligenciaArtificial #IAnaPratica #ChapterIA

---

## Copy pronto para produzir — #2 Anthropic + governo EUA (carrossel)
1. Capa — chip "IA E PODER" · "Por que o governo americano se preocupou com o Claude?"
2. O que aconteceu — "Os EUA suspenderam restrições que afetavam modelos avançados da Anthropic, após preocupações ligadas à cibersegurança." *(segundo reportagem)*
3. O contexto — "Quando uma IA fica poderosa o bastante, ela deixa de ser só produto e vira assunto de segurança nacional."
4. Por que importa pra você — "A IA que você usa no trabalho é a mesma tecnologia que governos monitoram. Entender isso é parte de usá-la bem."
5. A leitura ChapterIA — "Não é pra ter medo. É pra levar a sério: essa tecnologia é séria o suficiente pra mudar regras."
6. CTA — seguir / link bio.

*(As pautas 3–7 e 9 seguem o mesmo padrão branco quando aprovado o look.)*

---

# Lote 2 — pautas com fonte/imagem (Reuters / The Guardian)

> ✅ **STATUS: os 5 carrosséis foram finalizados** (fotos geradas por IA + composição).
> Artes em `assets/pauta/lote2-final/` (`L2F_pX_YY.png`) e mosaicos `L2F_pX_sheet.png`.

> ⚠️ **Imagens:** os arquivos precisam ser **anexados no chat** (a rede do ambiente
> bloqueia reuters.com e i.guim.co.uk). Cada capa usa a foto da respectiva notícia
> no template foto-ready. **Licenciamento:** fotos de agência exigem licença —
> avaliar uso próprio/banco licenciado antes de publicar de fato.

## #L2-1 · Claude Science (Carrossel · fundo branco · Alta)
Foto capa: Reuters/Dado Ruvic. Crédito visível no slide.
1. Capa — chip "IA NA CIÊNCIA" · "O Claude agora quer ajudar cientistas a pesquisar melhor." · sub: "E isso diz muito sobre o futuro do seu trabalho."
2. O QUE ACONTECEU — "A Anthropic lançou o Claude Science: uma área de trabalho com IA para organizar pesquisas, analisar dados e lidar com processos científicos complexos." *(Fonte: Reuters)*
3. POR QUE IMPORTA — "A IA está saindo do uso genérico e entrando em profissões específicas."
4. A TENDÊNCIA — "Cada setor vai ter seus próprios agentes e interfaces: ciência, saúde, direito, finanças."
5. NA PRÁTICA — "Não espere a IA 'geral' resolver tudo. Aprenda a moldar a IA pro seu contexto."
6. CTA — Siga @chapteria · Link na bio.
Legenda: A IA está deixando de ser 'ferramenta de texto' pra virar plataforma de trabalho por profissão. A Anthropic lançou o Claude Science pra pesquisa científica (Reuters) — e essa lógica vai chegar na sua área também. Quem aprende a adaptar a IA ao próprio trabalho sai na frente. #IA #ChapterIA

## #L2-2 · Meta: agentes mais devagar (Reels análise · Alta)
Foto/abertura: frame Reuters.
- HOOK (0–3s): "Até a Meta admitiu: agente de IA é mais difícil do que parece."
- (3–20s): "Internamente, Zuckerberg disse que o desenvolvimento de agentes não avançou na velocidade esperada. A empresa segue investindo pesado, mas os resultados ainda não vieram (Reuters)."
- (20–35s): "Tradução: agentes são uma tendência enorme — mas têm limitações reais. IA é oportunidade, não mágica."
- (35–45s): "Comece pelo que já funciona: automações simples e assistentes de tarefa. Não espere o 'agente perfeito'."
- CTA: "Segue pra aprender a usar o que já dá resultado hoje."
Legenda: Nem toda promessa de IA vira realidade na velocidade que vendem. Se até a Meta está apanhando com agentes, a lição é: foque no que já funciona. #IA #Agentes #ChapterIA

## #L2-3 · Samsung: bastidores da IA (Carrossel/Reels · Média)
Foto capa: Reuters/Kim Hong-Ji.
1. Capa — "Enquanto todos olham o ChatGPT, a Samsung lucra com os bastidores da IA."
2. O QUE ACONTECEU — "A Samsung projeta lucro operacional ~19x maior, puxado pela demanda de memória para infraestrutura de IA (DRAM, NAND, data centers)." *(Reuters)*
3. POR QUE IMPORTA — "A corrida da IA não é só software. É chip, memória, servidor e data center."
4. AS CAMADAS — "Os modelos (OpenAI, Anthropic, Google) rodam sobre uma infraestrutura gigante e cara."
5. NA PRÁTICA — "Entender as camadas te ajuda a enxergar oportunidades onde a maioria não olha."
6. CTA.
Legenda: A IA não movimenta só a OpenAI. Move chips, memória e data centers — e a Samsung acabou de mostrar isso no lucro (Reuters). Entender os bastidores é entender o mercado. #IA #ChapterIA

## #L2-4 · DeepMind: o filósofo (Carrossel denso · Média)
Imagem capa: ilustração Deena So'Oteh / The Guardian (crédito no slide).
1. Capa — "Por que uma das maiores empresas de IA tem um filósofo no time?"
2. QUEM — "The Guardian perfilou Iason Gabriel, filósofo no Google DeepMind."
3. O QUE ELE PENSA — "Alinhamento, ética, comportamento de agentes e impacto social da IA."
4. POR QUE IMPORTA — "Quando a IA decide, executa e influencia comportamento, o debate deixa de ser só técnico."
5. A LEITURA — "As empresas mais avançadas discutem valores e poder — não só performance."
6. PRA VOCÊ — "Usar IA com responsabilidade e critério também é competência."
7. CTA.
Legenda: As empresas mais avançadas de IA não discutem só tecnologia — discutem ética, comportamento e poder. Vale prestar atenção nisso. (Fonte: The Guardian) #IA #Etica #ChapterIA

## #L2-5 · Microsoft: 4.800 vagas (Carrossel/Reels autoridade · Alta)
Foto capa: Reuters/Gonzalo Fuentes.
1. Capa — "A Microsoft cortou 4.800 vagas e disse: a IA está mudando o trabalho." · sub: "Você está se preparando?"
2. O QUE ACONTECEU — "Corte de ~2,1% da força global, em uma reestruturação que inclui o Xbox. A empresa diz que os cargos não foram trocados diretamente por IA — mas reconhece que a IA muda como o trabalho é feito." *(Reuters)*
3. O PONTO REAL — "O risco não é só 'ser substituído por IA'. É não entender como o trabalho está mudando."
4. A VIRADA — "A IA reorganiza empresas: funções, custos e prioridades mudam de lugar."
5. PRA VOCÊ — "Quem entende e aplica IA vira o profissional que a empresa quer manter."
6. CTA.
Legenda: A Microsoft cortou 4.800 vagas e foi direta: a IA está mudando o trabalho (Reuters). O maior risco de carreira hoje não é a IA te substituir — é você não acompanhar. Bora se preparar. #Carreira #IA #ChapterIA
