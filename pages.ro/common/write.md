# write

> Scrieți un mesaj pe terminalul unui utilizator conectat specificat (Ctrl-C pentru a opri scrierea mesajelor).
> Utilizați comanda `who` pentru a afla toate terminal_idurile tuturor utilizatorilor activi activi în sistem. A se vedea, de asemenea, `mesg `

- Trimite un mesaj unui anumit utilizator pe un anumit id terminal:

`write {{username}} {{terminal_id}}`

- Trimite mesaj către „testuser” la terminalul `/dev/tty/5`:

`write {{testuser}} {{tty/5}}`

- Trimite mesaj către „johndoe” pe pseudo terminal `/dev/pts/5`:

`write {{johndoe}} {{pts/5}}`
