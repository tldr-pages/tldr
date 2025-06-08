# npm query

> Print een array van afhankelijkheidsobjecten met behulp van CSS-achtige selectors.
> Meer informatie: <https://docs.npmjs.com/cli/commands/npm-query>.

- Print directe afhankelijkheden:

`npm query ':root > *'`

- Print alle directe productie-/ontwikkelingsafhankelijkheden:

`npm query ':root > .{{prod|dev}}'`

- Print afhankelijkheden met een specifieke naam:

`npm query '#{{pakket}}'`

- Print afhankelijkheden met een specifieke naam en binnen een semantische versie range:

`npm query '#{{pakket}}@{{semantische_versie}}'`

- Print afhankelijkheden die geen andere afhankelijkheden hebben:

`npm query ':empty'`

- Zoek alle afhankelijkheden met postinstall-scripts en verwijder ze:

`npm query ":attr(scripts, [postinstall])" | jq 'map(.name) | join("\n")' {{[-r|--raw-output]}} | xargs -I _ npm uninstall _`

- Zoek alle Git-afhankelijkheden en print welke applicatie ze vereist:

`npm query ":type(git)" | jq 'map(.name)' | xargs -I _ npm why _`
