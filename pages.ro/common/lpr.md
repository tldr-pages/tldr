# lpr

> Instrumentul CUPS pentru tipărirea fișierelor.
> A se vedea, de asemenea, `lpstat` și `lpadmin` pentru listarea și configurarea imprimantelor.
> Mai multe informaţii: <http://www.CUPS.org>

- Imprimați un fișier la imprimanta implicită:

`lpr {{path/to/file}}`

- Tipărește 2 exemplare:

`lpr -# {{2}} {{path/to/file}}`

- Imprimați la o imprimantă numită:

`lpr -P {{printer}} {{path/to/file}}`

- Imprimați fie o singură pagină (de exemplu, 2), fie un interval de pagini (de exemplu, 2—16):

`lpr -o page-ranges={{2|2-16}} {{path/to/file}}`

- Imprimați față-verso, fie în portret (lung), fie în peisaj (scurt):

`lpr -o sides={{two_sided_long_edge|two_sided_short_edge}} {{path/to/file}}`

- Setați dimensiunea paginii (pot fi disponibile mai multe opțiuni în funcție de configurare):

`lpr -o media={{a4|letter|legal}} {{path/to/file}}`

- Imprimați mai multe pagini pe foaie:

`lpr -o number-up={{2|4|6|9|16}} {{path/to/file}}`
