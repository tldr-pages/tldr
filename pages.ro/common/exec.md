# exec

> Înlocuiți procesul curent cu un alt proces.

- Înlocuiți cu comanda specificată utilizând variabilele actuale de mediu:

`exec {{command -with -flags}}`

- Înlocuiți cu comanda specificată, variabilele de compensare a mediului:

`exec -c {{command -with -flags}}`

- Înlocuiți cu comanda specificată și autentificați-vă utilizând shell-ul implicit:

`exec -l {{command -with -flags}}`

- Înlocuiți cu comanda specificată și schimbați numele procesului:

`exec -a {{process_name}} {{command -with -flags}}`
