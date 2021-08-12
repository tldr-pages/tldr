# extrace

> Trasare exec () apeluri.
> Mai multe informaţii: <https://github.com/chneukirchen/extrace>

- Urmăriți toate execuțiile programului care au loc pe sistem:

`sudo extrace`

- Rulați o comandă și urmăriți numai descendenții acestei comenzi:

`sudo extrace {{command}}`

- Imprimați directorul curent de lucru al fiecărui proces:

`sudo extrace -d`

- Rezolvați calea completă a fiecărui executabil:

`sudo extrace -l`

- Afișează utilizatorul care rulează fiecare proces:

`sudo extrace -u`
