# export

> Befehl zum Markieren von Shell-Variablen in der aktuellen Umgebung, die mit allen neu gegabelten Unterprozessen exportiert werden sollen.
> Weitere Informationen: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- Lege eine neue Umgebungsvariable fest:

`export {{variable}}={{wert}}`

- Entferne eine Umgebungsvariable:

`export -n {{variable}}`

- Markiere eine Shell-Funktion für den Export:

`export -f {{funktionsname}}`

- Hänge etwas an die Pfad-Variable an:

`export PATH=$PATH:{{pfad/zu/anhängen}}`
