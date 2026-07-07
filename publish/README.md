# Publicação no Instagram — setup

Automatiza a publicação dos posts (carrossel ou imagem única) via **Instagram
Graph API**, rodando no **GitHub Actions** (a rede deste ambiente de dev bloqueia
a API da Meta; o Actions roda com internet aberta).

> Nada é publicado sozinho: o workflow é **manual** (botão *Run workflow*).
> Só vira automático se você configurar um agendamento depois.

## Pré-requisitos na Meta (você faz uma vez)

1. **Conta Instagram Profissional** (Business ou Creator).
2. **Página do Facebook** vinculada a essa conta do Instagram.
3. **App no Meta for Developers** (developers.facebook.com) do tipo *Business*.
4. Produto **Instagram Graph API** adicionado ao app.
5. Permissões: `instagram_basic`, `instagram_content_publish`, `pages_show_list`,
   `pages_read_engagement`, `business_management`.
6. **Token de acesso de longa duração** (long-lived, ~60 dias) do usuário/página.
7. Descobrir o **Instagram Business Account ID** (o `IG_USER_ID`):
   `GET /me/accounts` → pega o Page ID → `GET /{page-id}?fields=instagram_business_account`.

> ⚠️ **App Review:** para publicar em contas fora do "modo de teste", a Meta exige
> App Review de `instagram_content_publish` + verificação do negócio (pode levar
> dias). Com você como admin/tester do app, dá para testar na sua própria conta
> antes disso.

## Configurar no GitHub (repositório fepela/lis)

1. **Settings → Secrets and variables → Actions → New repository secret**:
   - `IG_USER_ID` = seu Instagram Business Account ID
   - `IG_ACCESS_TOKEN` = o token de longa duração
2. Se o repositório for **público**, abra
   [`.github/workflows/publish-instagram.yml`](../.github/workflows/publish-instagram.yml)
   e descomente a linha `RAW_BASE:` (usa as URLs raw do GitHub — mais simples).
   Se for **privado**, deixe como está (o script sobe as imagens para um host
   público temporário, porque a Meta não lê imagens de repo privado).

## Publicar um post

1. No GitHub: aba **Actions → "Publicar no Instagram" → Run workflow**.
2. Preencha **post_path**, ex.: `social/posts/2026-07-07/01-claude-sonnet5`.
3. Marque **dry_run** na primeira vez para testar sem publicar (ele resolve e
   mostra as URLs das imagens). Depois rode sem o dry-run para publicar.

O script usa as artes `01.png, 02.png, …` da pasta (na ordem) e a seção
`## Legenda` do `README.md` do post como legenda.

## Rodar localmente (opcional)

```bash
pip install requests
export IG_USER_ID=...   IG_ACCESS_TOKEN=...
python publish/instagram_publish.py social/posts/2026-07-07/01-claude-sonnet5 --dry-run
```

## Limites e observações
- Carrossel: **2 a 10 imagens** (nossos posts respeitam isso).
- Legenda: até ~2.200 caracteres.
- A API publica **imagens** (JP/PNG). Para Reels/vídeo o fluxo é outro (dá para
  adicionar depois).
- Rate limit de publicação: ~25 posts por conta / 24h.
- Renove o token antes de expirar (a cada ~60 dias) ou automatize a renovação.
