# dirs

> Afișează sau manipulează stiva directorului.
> Stiva de directoare este o listă de directoare recent vizitate care pot fi manipulate cu comenzile `pushd` și `popd`.
> Mai multe informaţii: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>

- Afișează stiva directorului cu un spațiu între fiecare intrare:

`dirs`

- Afișează stiva directorului cu o singură intrare pe linie:

`dirs -p`

- Afișează numai intrarea n-a în stiva directorului, începând de la 0:

`dirs +{{N}}`

- Ștergeți stiva directorului:

`dirs -c`
