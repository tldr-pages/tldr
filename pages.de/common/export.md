# export

> Befehl zum Markieren von Shell-Variablen in der aktuellen Umgebung, die mit allen neu abgezweigten Unterprozessen exportiert werden sollen.
> Weitere Informationen: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#export>.

- Lege eine neue Umgebungsvariable fest:

`export {{variable}}={{wert}}`

- Entferne eine Umgebungsvariable:

`export -n {{variable}}`

- Markiere eine Shell-Funktion für den Export:

`export -f {{funktionsname}}`

- Hänge etwas an die PATH-Variable an:

`export PATH=$PATH:{{pfad/zu/anhängen}}`
