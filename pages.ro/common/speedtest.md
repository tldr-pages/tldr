# speedtest

> Interfață oficială de linie de comandă pentru testarea lățimii de bandă pe internet utilizând https://speedtest.net.
> Notă: unele platforme leagă `speedtest` la `speedtest-cli`. Dacă unele dintre exemplele din această pagină nu funcționează, consultați `speedtest-cli`.
> Mai multe informaţii: <https://www.speedtest.net/apps/cli>

- Rulați un test de viteză:

`speedtest`

- Rulați un test de viteză și specificați unitatea de ieșire:

`speedtest --unit={{auto-decimal-bits|auto-decimal-bytes|auto-binary-bits|auto-binary-bytes}}`

- Rulați un test de viteză și specificați formatul de ieșire:

`speedtest --format={{human-readable|csv|tsv|json|jsonl|json-pretty}}`

- Rulați un test de viteză și specificați numărul de zecimale de utilizat (0 la 8, valorile implicite la 2):

`speedtest --precision={{precision}}`

- Rulați un test de viteză și imprimați progresul acestuia (disponibil numai pentru formatul de ieșire „ușor de citit de om' și `json`):

`speedtest --progress={{yes|no}}`

- Listează toate serverele `speedtest.net, sortate după distanță:

`speedtest --servers`

- Rulați un test de viteză pe un anumit server `speedtest.net:

`speedtest --server-id={{server_id}}`
