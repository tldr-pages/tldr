# az config

> Verwalten der der Azure CLI-Konfiguration.
> Teil der `Azure CLI`, der Befehlszeilenschnittstelle von Azure.
> Mehr Informationen: <https://learn.microsoft.com/cli/azure/config>.

- Rufen Sie alle Konfigurationen ab:

`az config get`

- Rufen Sie alle Konfigurationen in einem Abschnitt ab:

`az config get {{sektionsname}}`

- Legen Sie eine Konfiguration fest:

`az config set {{konfigurationsname}}={{wert}}`

- Heben Sie eine Konfiguration auf:

`az config unset {{konfigurationsname}}`
