# cut

> Decupați câmpurile din stdin sau fișiere.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/cut>

- Tăiați primele șaisprezece caractere ale fiecărei linii de stdin:

`cut -c {{1-16}}`

- Tăiați primele șaisprezece caractere ale fiecărei linii a fișierelor date:

`cut -c {{1-16}} {{file}}`

- Tăiați totul de la al treilea caracter până la sfârșitul fiecărei linii:

`cut -c {{3-}}`

- Decupați al cincilea câmp al fiecărei linii, folosind un colon ca delimitator de câmp (delimitatorul implicit este fila):

`cut -d'{{:}}' -f{{5}}`

- Tăiați câmpurile 2 și 10 ale fiecărei linii, folosind un punct și virgulă ca delimitator:

`cut -d'{{;}}' -f{{2,10}}`

- Tăiați câmpurile 3 până la sfârșitul fiecărei linii, folosind un spațiu ca delimitator:

`cut -d'{{ }}' -f{{3-}}`
