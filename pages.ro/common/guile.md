# guile

> Interpretul schemei de viclenie.
> Mai multe informaţii: <https://www.gnu.org/software/guile>

- Porniți schema de Guile REPL:

`guile`

- Executați scriptul într-un fișier Schema dat:

`guile {{script.scm}}`

- Execută o expresie a schemei:

`guile -c "{{expression}}"`

- Ascultați pe un port sau un socket de domeniu Unix (implicit este portul 37146) pentru conexiuni REPL la distanță:

`guile --listen={{port_or_socket}}`
