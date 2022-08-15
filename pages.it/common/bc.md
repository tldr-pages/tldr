# bc

> Calcolatore.
> Maggiori informazioni: <https://manned.org/man/bc.1>.

- Esegui in modalità interattiva utilizzando la libreria math della standard library:

`bc -l`

- Calcola il risultato di un'espressione:

`bc <<< "(1 + 2) * 2 ^ 2"`

- Calcola un'espressione forzando il numero di decimali usati a 10:

`bc <<< "scale=10; 5 / 3"`

- Calcola un'espressione con seno e coseno utilizzando mathlib:

`bc -l <<< "s(1) + c(1)"`
