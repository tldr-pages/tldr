# choco uninstall

> Verwijder een of meerdere pakketen met Chocolatey.
> Meer informatie: <https://chocolatey.org/docs/commands-uninstall>.

- Verwijder een of meerdere spatie-gescheiden pakketten:

`choco uninstall {{pakket1 pakket2 ...}}`

- Verwijder een specifieke versie van een pakket:

`choco uninstall {{pakket}} --version {{versie}}`

- Bevestig alle prompts automatisch:

`choco uninstall {{pakket}} --yes`

- Verwijder alle afhankelijkheden bij het verwijderen:

`choco uninstall {{pakket}} --remove-dependencies`

- Verwijder alle pakketten:

`choco uninstall all`
