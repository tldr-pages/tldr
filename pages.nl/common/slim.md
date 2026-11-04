# slim

> Analyseer en optimaliseer Docker-images.
> Meer informatie: <https://github.com/slimtoolkit/slim#usage-details>.

- Start Slim in interactieve modus:

`slim`

- Analyseer Docker-lagen van een specifieke image:

`slim xray --target {{image:tag}}`

- Lint een Dockerfile:

`slim lint --target {{pad/naar/Dockerfile}}`

- Analyseer en genereer een geoptimaliseerde Docker-image:

`slim build {{image:tag}}`

- Toon de help voor een subcommando:

`slim {{subcommando}} --help`
