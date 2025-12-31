# tldr

> Toon simpele hulppagina's voor command-line programma's uit het tldr-pages project.
> Opmerking: De opties `--language` en `--list` zijn niet vereist door de clientspecificatie, maar de meeste clients implementeren ze wel.
> Meer informatie: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Toon de tldr-pagina voor een specifiek commando (hint: dit is hoe je hier bent gekomen!):

`tldr {{commando}}`

- Toon de tldr-pagina voor een specifiek subcommando:

`tldr {{commando}} {{subcommando}}`

- Toon de tldr-pagina voor een commando in de opgegeven taal (indien beschikbaar, val anders terug op Engels):

`tldr {{[-L|--language]}} {{taalcode}} {{commando}}`

- Toon de tldr-pagina voor een commando van een specifiek platform:

`tldr {{[-p|--platform]}} {{android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows}} {{commando}}`

- Update de lokale cache van tldr-pagina's:

`tldr {{[-u|--update]}}`

- Toon alle pagina's voor het huidige platform en `common`:

`tldr {{[-l|--list]}}`

- Toon alle beschikbare subcommandopagina's voor een commando:

`tldr {{[-l|--list]}} | grep {{commando}} | column`

- Toon de tldr-pagina voor een willekeurig commando:

`tldr {{[-l|--list]}} | shuf {{[-n|--head-count]}} 1 | xargs tldr`
