# choco uninstall

> Odinstalowanie jednego lub więcej pakietów zarządzanych przez Chocolatey.
> Więcej informacji: <https://chocolatey.org/docs/commands-uninstall>.

- Odinstalowanie jednego lub więcej pakietów (oddzielonych spacją):

`choco uninstall {{{pakiet(pakietów)}}`

- Odinstalowanie konkretnej wersji pakietu:

`choco uninstall {{pakiet}} --version {{wersja}}`

- Automatyczna akceptacja wszystkich monitów podczas deinstalacji pakietu:

`choco uninstall {{pakiet}} --yes`

- Odinstalowanie wszystkich zależności podczas procesu deinstalacji danego pakietu/pakietów:

`choco uninstall {{pakiet}} --remove-dependencies`

- Odinstalowanie wszystkich pakietów:

`choco uninstall all`
