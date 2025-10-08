# npm exec

> Voer binaire bestanden uit vanuit `npm`-pakketten.
> Meer informatie: <https://docs.npmjs.com/cli/npm-exec>.

- Voer het commando uit vanuit een lokaal of extern `npm`-pakket:

`npm {{[x|exec]}} {{commando}} {{argument1 argument2 ...}}`

- Specificeer het pakket expliciet (handig als meerdere commando's dezelfde naam hebben):

`npm {{[x|exec]}} --package {{pakket}} {{commando}}`

- Voer een commando uit als het bestaat in het huidig pad of in `node_modules/.bin`:

`npm {{[x|exec]}} --no-install {{commando}} {{argument1 argument2 ...}}`

- Voer een specifiek commando uit, waarbij uitvoer van `npm` zelf wordt onderdrukt:

`npm {{[x|exec]}} --quiet {{command}} {{argument1 argument2 ...}}`

- Toon de help:

`npm {{[x|exec]}} --help`
