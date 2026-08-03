# choco list

> Toon een lijst van lokaal geïnstalleerde pakketten met Chocolatey.
> Meer informatie: <https://docs.chocolatey.org/en-us/choco/commands/list/>.

- Toon lokaal geïnstalleerde pakketten:

`choco list`

- Toon geïnstalleerde inclusief systeemprogramma's:

`choco list {{[-i|--include-programs]}}`

- Toon alleen de ID's van de geïnstalleerde pakketten:

`choco list --id-only`

- Toon geïnstalleerde pakketten die exact overeenkomen met een naam:

`choco list {{pakket}} {{[-e|--exact]}}`

- Toon geïnstalleerde pakketten die beginnen met een specifieke voorvoegsel:

`choco list --id-starts-with {{voorvoegsel}}`

- Toon geïnstalleerde pakketten van een alternatieve bron:

`choco list {{[-s|--source]}} {{windowsfeatures|ruby|cygwin|...}}`
