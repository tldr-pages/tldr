# shellcheck

> Shell script instrument de analiză statică.
> Verificați scripturile shell pentru erori, utilizarea caracteristicilor deprecate/nesigure și practici greșite.
> Mai multe informaţii: <https://www.shellcheck.net>

- Verifică un script shell:

`shellcheck {{path/to/script.sh}}`

- Verificați un script shell interpretându-l ca dialect shell specificat (suprascrie shebang în partea de sus a script-ului):

`shellcheck --shell {{sh|bash|dash|ksh}} {{path/to/script.sh}}`

- Ignorați unul sau mai multe tipuri de erori:

`shellcheck --exclude {{SC1009,SC1073}} {{path/to/script.sh}}`

- Verificați, de asemenea, orice script-uri de shell provenite:

`shellcheck --checked-sourced {{path/to/script.sh}}`

- Afișarea ieșirii în formatul specificat (implicit la `tty`):

`shellcheck --format {{tty|checkstyle|diff|gcc|json|json1|quiet}} {{path/to/script.sh}}`

- Activați una sau mai multe verificări opționale:

`shellcheck --enable={{add-default-case|avoid-nullary-conditions}}`

- Listează toate verificările opționale disponibile care sunt dezactivate în mod implicit:

`shellcheck --list-optional`
