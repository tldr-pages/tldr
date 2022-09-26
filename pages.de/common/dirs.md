# dirs

> Zuletzt besuchte Ordner anzeigen und verändern.
> Die Liste der zuletzt besuchten Ordner kann mit `pushd` und `popd` verändert werden.
> Weitere Informationen: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- Zeige die zuletzt besuchten Ordner durch Leerzeichen getrennt an:

`dirs`

- Zeige die zuletzt besuchten Ordner mit einem Eintrag pro Zeile an:

`dirs -p`

- Zeige den N-ten Eintrag der zuletzt besuchten Ordner an, beginnend mit 0:

`dirs +{{N}}`

- Leere die Liste der zuletzt besuchten Ordner:

`dirs -c`
