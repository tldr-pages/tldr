# npm install-test

> Equivalent aan het uitvoeren van `npm install` gevolgd door `npm test`.
> Opmerking: `it` kan gebruikt worden als afkorting voor `install-test`.
> Meer informatie: <https://docs.npmjs.com/cli/npm-install-test/>.

- Installeer alle afhankelijkheden en voer vervolgens tests uit:

`npm {{[it|install-test]}}`

- Installeer een specifiek pakket en voer vervolgens tests uit:

`npm {{[it|install-test]}} {{pakket_naam}}`

- Installeer een pakket en sla het op als afhankelijkheid voordat de tests worden uitgevoerd:

`npm {{[it|install-test]}} {{pakket_naam}} {{[-S|--save]}}`

- Installeer afhankelijkheden globaal en voer vervolgens tests uit:

`npm {{[it|install-test]}} {{[-g|--global]}}`
