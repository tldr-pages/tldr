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

`tldr {{[-p|--platform]}} {{android|cisco-ios|common|dos|freebsd|linux|netbsd|openbsd|osx|sunos|windows}} {{commando}}`

- Update de lokale cache van tldr-pagina's:

`tldr {{[-u|--update]}}`

- Toon alle pagina's voor het huidige platform en `common`:

`tldr {{[-l|--list]}}`

- Blader door tldr-pagina's in een terminalvenster (`fzf` moet beschikbaar zijn):

`tldr {{[-l|--list]}} | fzf --preview "tldr {1} --color=always" --preview-window=right,70% | xargs tldr`

- Toon de tldr-pagina voor een willekeurig commando:

`tldr {{[-l|--list]}} | shuf {{[-n|--head-count]}} 1 | xargs tldr`
