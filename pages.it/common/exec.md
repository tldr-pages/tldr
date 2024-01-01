# exec

> Sostituisci il processo corrente con un altro.
> Maggiori informazioni: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#exec>.

- Sostituisci con il comando specificato utilizzando le variabili di ambiente correnti:

`exec {{comando -con -flag}}`

- Sostituisci con il comando specificato utilizzando un ambiente vuoto:

`exec -c {{comando -con -flag}}`

- Sostituisci con il comando specificato ed esegui il login con la shell predefinita:

`exec -l {{comando -con -flag}}`

- Sostituisci con il comando specificato e cambia il nome del processo:

`exec -a {{nuovo_nome_processo}} {{comando -con -flag}}`
