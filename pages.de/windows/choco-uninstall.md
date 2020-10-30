# choco uninstall

> Deinstalliere mit Chocolatey ein oder mehrere Pakete.
> Mehr Informationen: <https://chocolatey.org/docs/commands-uninstall>.

- Deinstalliere ein oder mehrere Pakete, deren Namen mit Leerzeichen getrennt sind:

`choco uninstall {{paket(e)}}`

- Deinstalliere eine bestimmte Version eines Paketes:

`choco uninstall {{paket}} --version {{version}}`

- Stimme allen Fragen automatisch zu:

`choco uninstall {{paket}} --yes`

- Deinstalliere auch alle Abhängigkeiten:

`choco uninstall {{paket}} --remove-dependencies`

- Deinstalliere alle Pakete:

`choco uninstall all`
