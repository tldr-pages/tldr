# pulumi up

> Creëer of update de bronnen in een stack.
> Meer informatie: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_up/>.

- Bekijk en implementeer wijzigingen in een programma en/of infrastructuur:

`pulumi up`

- Keur de update automatisch goed en voer deze uit na het bekijken van de voorvertoning:

`pulumi up {{[-y|--yes]}}`

- Bekijk en implementeer wijzigingen in een specifieke stack:

`pulumi up {{[-s|--stack]}} {{stack}}`

- Ververs de status van de bronnen van de stack voor het updaten:

`pulumi up {{[-r|--refresh]}}`

- Toon de stack-uitvoer niet:

`pulumi up --suppress-outputs`

- Ga door met het updaten van de bronnen, zelfs als er een fout optreedt:

`pulumi up --continue-on-error`

- Toon de help:

`pulumi up {{[-h|--help]}}`
