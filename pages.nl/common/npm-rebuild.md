# npm rebuild

> Herbouw native Node.js-pakketten na wijzigingen aan Node of afhankelijkheden.
> Meer informatie: <https://docs.npmjs.com/cli/npm-rebuild/>.

- Herbouw een specifiek pakket:

`npm {{[rb|rebuild]}} {{pakket}}`

- Herbouw alle geïnstalleerde pakketten:

`npm {{[rb|rebuild]}}`

- Herbouw met uitgebreide uitvoer:

`npm {{[rb|rebuild]}} --verbose`

- Herbouw een pakket in een specifieke map:

`npm {{[rb|rebuild]}} --prefix {{pad/naar/map}} {{pakket}}`

- Herbouw zonder de npm-cache te gebruiken:

`npm {{[rb|rebuild]}} --no-cache`

- Herbouw in globale modus:

`npm {{[rb|rebuild]}} {{[-g|--global]}}`
