# az config

> Verwalten der Azure CLI-Konfiguration.
> Teil von `azure-cli` (auch bekannt als `az`).
> Weitere Informationen: <https://learn.microsoft.com/en-us/cli/azure/config?view=azure-cli-latest>.

- Rufe alle Konfigurationen ab:

`az config get`

- Rufe alle Konfigurationen in einer Sektion ab:

`az config get {{sektionsname}}`

- Setze eine Konfiguration:

`az config set {{konfigurationsname}}={{wert}}`

- Hebe eine Konfiguration auf:

`az config unset {{konfigurationsname}}`
