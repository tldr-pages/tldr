# chsh

> Cambia la shell di login di un utente.
> Fa parte di `util-linux`.
> Maggiori informazioni: <https://manned.org/chsh>.

- Imposta interattivamente una shell di login per l'utente corrente:

`chsh`

- Elenca le shell disponibili:

`chsh {{[-l|--list-shells]}}`

- Imposta una shell di login specifica per l'utente corrente:

`chsh {{[-s|--shell]}} {{percorso/alla/shell}}`

- Imposta la shell di login per un utente specifico:

`sudo chsh {{[-s|--shell]}} {{percorso/alla/shell}} {{username}}`
