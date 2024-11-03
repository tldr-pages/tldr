# npm

> JavaScript en Node.js pakketbeheerder.
> Beheer Node.js-projecten en hun module-afhankelijkheden.
> Meer informatie: <https://www.npmjs.com>.

- Maak een `package.json`-bestand met standaardwaarden (laat --yes weg om dit interactief te doen):

`npm init {{-y|--yes}}`

- Download alle pakketten die zijn vermeld als afhankelijkheden in `package.json`:

`npm install`

- Download een specifieke versie van een pakket en voeg het toe aan de lijst van afhankelijkheden in `package.json`:

`npm install {{pakket_naam}}@{{versie}}`

- Download de nieuwste versie van een pakket en voeg het toe aan de lijst van dev-afhankelijkheden in `package.json`:

`npm install {{pakket_naam}} {{-D|--save-dev}}`

- Download de nieuwste versie van een pakket en installeer het globaal:

`npm install {{-g|--global}} {{pakket_naam}}`

- Verwijder een pakket en haal het uit de lijst van afhankelijkheden in `package.json`:

`npm uninstall {{pakket_naam}}`

- Toon alle lokaal geïnstalleerde afhankelijkheden:

`npm list`

- Toon alle top-level globaal geïnstalleerde pakketten:

`npm list {{-g|--global}} --depth {{0}}`
