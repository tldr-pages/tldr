# csplit

> Împărțiți un fișier în bucăți.
> Aceasta generează fișiere numite „xx00", „xx01" și așa mai departe.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/csplit>

- Împărțiți un fișier la liniile 5 și 23:

`csplit {{file}} {{5}} {{23}}`

- Împărțiți un fișier la fiecare 5 linii (acest lucru va eșua dacă numărul total de linii nu este divizibil cu 5):

`csplit {{file}} {{5}} {*}`

- Împărțiți un fișier la fiecare 5 linii, ignorând eroarea exactă de diviziune:

`csplit -k {{file}} {{5}} {*}`

- Împărțiți un fișier la linia 5 și utilizați un prefix personalizat pentru fișierele de ieșire:

`csplit {{file}} {{5}} -f {{prefix}}`

- Împărțiți un fișier la o linie care corespunde unei expresii regulate:

`csplit {{file}} /{{regular_expression}}/`
