# fold

> Împachetează fiecare linie dintr-un fișier de intrare pentru a se potrivi cu o lățime specificată și o imprimă la ieșirea standard.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/fold>

- Înfășurați fiecare linie la lățimea implicită (80 caractere):

`fold {{file}}`

- Înfășurați fiecare linie la lățimea „30":

`fold -w30 {{file}}`

- Înfășurați fiecare linie la lățimea „5" și rupeți linia la spații (pune fiecare spațiu separat cuvânt într-o linie nouă, cuvintele cu lungimea > 5 sunt înfășurate):

`fold -w5 -s {{file}}`
