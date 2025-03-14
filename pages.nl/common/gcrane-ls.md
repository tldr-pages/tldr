# gcrane ls

> Toon de tags in een repository.
> Complexere vorm dan `crane ls`, die het mogelijk maakt om tags, manifesten en sub-repositories te tonen.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Toon de tags:

`gcrane ls {{repository}}`

- Formatteer de reactie van de registry als JSON:

`gcrane ls {{repository}} --json`

- Of door repositories te recursief te doorlopen:

`gcrane ls {{repository}} {{[-r|--recursive]}}`

- Toon de help:

`gcrane ls {{[-h|--help]}}`
