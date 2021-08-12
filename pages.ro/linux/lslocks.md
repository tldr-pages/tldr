# lslocks

> Lista blocurilor locale de sistem.

- Listează toate încuietorile locale ale sistemului:

`lslocks`

- Lista blocurilor cu anteturi de coloană definite:

`lslocks --output {{PID}},{{COMMAND}},{{PATH}}`

- Listează blocări care produc o ieșire brută (fără coloane) și fără anteturi de coloană:

`lslocks --raw --noheadings`

- Lista blocurilor prin introducerea PID:

`lslocks --pid {{PID}}`

- Lista de încuietori cu ieșire json la stdout:

`lslocks --json`
