# guile

> Guile Scheme interpreter. További információ: <https://www.gnu.org/software/guile>.

- REPL (interaktív shell) indítása:

`guile`

- Egy adott Scheme fájlban lévő szkript végrehajtása:

`guile {{script.scm}}`

- Scheme kifejezés végrehajtása:

`guile -c "{{expression}}"`

- Egy porton vagy egy Unix tartományi aljzaton (az alapértelmezett a 37146-os port) figyel a távoli REPL-kapcsolatokra:

`guile --listen={{port_or_socket}}`
