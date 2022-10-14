# choco uninstall

> Odinstalowanie jednego lub więcej pakietów zarządzanych przez Chocolatey.
> Więcej informacji: <https://chocolatey.org/docs/commands-uninstall>.

- Odinstalowanie jednego lub więcej pakietów (oddzielonych spacją):

`choco uninstall {{nazwa_pakietu(pakietów)}}`

- Odinstalowanie konkretnej wersji pakietu:

`choco uninstall {{nazwa_pakietu}} --version {{wersja}}`

- Automatyczna akceptacja wszystkich monitów podczas deinstalacji pakietu (--yes):

`choco uninstall {{nazwa_pakietu(pakietów)}} --yes`

- Odinstalowanie wszystkich zależności podczas procesu deinstalacji danego pakietu/pakietów:

`choco uninstall {{nazwa_pakietu(pakietów)}} --remove-dependencies`

- Odinstalowanie wszystkich pakietów:

`choco uninstall all`