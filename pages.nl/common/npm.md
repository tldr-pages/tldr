# npm

> JavaScript en Node.js pakketbeheer.
> Beheer Node.js-projecten en hun module-afhankelijkheden.
> Sommige subcommando's zoals `install`, `run`, etc. hebben hun eigen documentatie.
> Meer informatie: <https://docs.npmjs.com/cli/npm/>.

- Maak een `package.json`-bestand met standaardwaarden (laat `--yes` weg om dit interactief te doen):

`npm init {{[-y|--yes]}}`

- Download alle pakketten die zijn vermeld als afhankelijkheden in `package.json`:

`npm {{[i|install]}}`

- Download een specifieke versie van een pakket en voeg het toe aan de lijst van afhankelijkheden in `package.json`:

`npm {{[i|install]}} {{pakket_naam}}@{{versie}}`

- Download de nieuwste versie van een pakket en voeg het toe aan de lijst van dev-afhankelijkheden in `package.json`:

`npm {{[i|install]}} {{pakket_naam}} {{[-D|--save-dev]}}`

- Download de nieuwste versie van een pakket en installeer het globaal (stel de installatielocatie in met `npm config set prefix`):

`npm {{[i|install]}} {{pakket_naam}} {{[-g|--global]}}`

- Verwijder een pakket en haal het uit de lijst van afhankelijkheden in `package.json`:

`npm {{[r|uninstall]}} {{pakket_naam}}`

- Toon alle lokaal geïnstalleerde afhankelijkheden:

`npm {{[ls|list]}}`

- Toon alle top-level globaal geïnstalleerde pakketten:

`npm {{[ls|list]}} {{[-g|--global]}} --depth {{0}}`
