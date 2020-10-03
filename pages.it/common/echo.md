# echo

> Stampa a schermo gli argomenti forniti.

- Stampa un messaggio di testo. Nota: le virgolette sono opzionali:

`echo "{{Hello World}}"`

- Stampa un messaggio con il contenuto di variabili di ambiente:

`echo "{{La mia path è $PATH}}"`

- Stampa un messaggio senza il carattere di nuova linea finale:

`echo -n "{{Hello World}}"`

- Aggiungi un messaggio in coda ad un file:

`echo "{{Hello World}}" >> {{file.txt}}`

- Abilita l'interpretazione delle sequenze di escape con il backslash (caratteri speciali):

`echo -e "{{Colonna 1\tColonna 2}}"`
