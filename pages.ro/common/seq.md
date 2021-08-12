# seq

> Ieșiți o secvență de numere la stdout.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/seq>

- Secvență de la 1 la 10:

`seq 10`

- Fiecare al treilea număr de la 5 la 20:

`seq 5 3 20`

- Separați ieșirea cu un spațiu în loc de o linie nouă:

`seq -s " " 5 3 20`

- Formatarea lățimii de ieșire la un minim de 4 cifre de umplutură cu zerouri, după cum este necesar:

`seq -f "%04g" 5 3 20`
