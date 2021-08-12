# uniq

> Ieșiți liniile unice din intrarea sau fișierul dat.
> Din moment ce nu detectează linii repetate, cu excepția cazului în care sunt adiacente, trebuie să le sorteze mai întâi.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/uniq>

- Afișează fiecare linie o dată:

`sort {{file}} | uniq`

- Afișează numai linii unice:

`sort {{file}} | uniq -u`

- Afișează numai linii duplicate:

`sort {{file}} | uniq -d`

- Afișează numărul de apariții ale fiecărei linii împreună cu acea linie:

`sort {{file}} | uniq -c`

- Afișează numărul de apariții ale fiecărei linii, sortate după cele mai frecvente:

`sort {{file}} | uniq -c | sort -nr`
