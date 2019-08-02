# env

> Mostra le variabili d'ambiente o esegui un programma in un ambiente modificato.

- Mostra le variabili d'ambiente:

`env`

- Esegui un programma. Utilizzato spesso in script dopo lo shebang (#!) per cercare il percorso del programma:

`env {{programma}}`

- Resetta l'ambiente ed esegui un programma:

`env -i {{programma}}`

- Rimuovi una variabile dall'ambiente ed esegui un programma:

`env -u {{variabile}} {{programma}}`

- Setta una variabile ed esegui un programma:

`env {{variabile}}={{valore}} {{programma}}`
