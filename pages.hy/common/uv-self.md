# ուլտրամանուշակագույն ինքնություն

> Կառավարեք `uv` գործադիրն ինքնին:.
> Լրացուցիչ տեղեկություններ. <https://docs.astral.sh/uv/reference/cli/#uv-self>:.

- Թարմացրեք `uv`-ը վերջին տարբերակին՝:

`uv self update`

- Թարմացրեք `uv`-ը որոշակի տարբերակի.:

`uv self update {{0.4.0}}`

- Ստուգեք մատչելի `uv` թարմացումները՝ առանց տեղադրելու՝:

`uv self update --dry-run`

- Թարմացրեք `uv`-ը բովանդակալից ելքով.:

`uv self update {{[-v|--verbose]}}`

- Ցուցադրել ընթացիկ `uv` տարբերակը.:

`uv self version`

- Ցուցադրել միայն տարբերակի համարը.:

`uv self version --short`

- Ցուցադրել տարբերակը JSON ձևաչափով.:

`uv self version --output-format json`
