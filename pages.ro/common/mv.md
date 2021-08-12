# mv

> Mutați sau redenumiți fișiere și directoare.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/mv>

- Mutați un fișier într-o locație arbitrară:

`mv {{source}} {{target}}`

- Mutați fișierele într-un alt director, păstrând numele fișierelor:

`mv {{source1}} {{source2}} {{source3}} {{target_directory}}`

- Nu solicitați confirmarea înainte de suprascrierea fișierelor existente:

`mv -f {{source}} {{target}}`

- Solicitați confirmarea înainte de suprascrierea fișierelor existente, indiferent de permisiunile fișierului:

`mv -i {{source}} {{target}}`

- Nu suprascrieți fișierele existente la țintă:

`mv -n {{source}} {{target}}`

- Mutați fișierele în modul verbose, afișând fișierele după ce sunt mutate:

`mv -v {{source}} {{target}}`
