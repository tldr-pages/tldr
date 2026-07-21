# ip rule

> Gestione del database delle politiche di routing IP.
> Maggiori informazioni: <https://manned.org/ip-rule>.

- Mostra la politica di routing:

`ip {{[ru|rule]}}`

- Crea una nuova regola di routing generica con priorità più alta di `main`:

`sudo ip {{[ru|rule]}} {{[a|add]}} from all lookup {{table_id}}`

- Aggiunge una nuova regola basata sugli indirizzi sorgente del pacchetto:

`sudo ip {{[ru|rule]}} {{[a|add]}} from {{192.168.178.2/32}} lookup {{table_id}}`

- Aggiunge una nuova regola basata sugli indirizzi di destinazione del pacchetto:

`sudo ip {{[ru|rule]}} {{[a|add]}} to {{192.168.178.2/32}} lookup {{table_id}}`

- Elimina una regola basata sugli indirizzi sorgente del pacchetto:

`sudo ip {{[ru|rule]}} {{[d|delete]}} from {{192.168.178.2/32}}`

- Rimuove tutte le regole di routing:

`sudo ip {{[ru|rule]}} {{[f|flush]}}`

- Salva tutte le regole in un file:

`ip {{[ru|rule]}} {{[s|save]}} > {{path/to/ip_rules.dat}}`

- Ripristina tutte le regole da un file:

`sudo ip < {{path/to/ip_rules.dat}} {{[ru|rule]}} {{[r|restore]}}`
