# doggo

> Cliente DNS para Humanos.
> Escrito en Golang.
> Más información: <https://github.com/mr-karan/doggo>.

- Realiza una simple búsqueda DNS:

`doggo {{example.com}}`

- Consulta registros MX usando un servidor de nombres específico:

`doggo MX {{codeberg.org}} @{{1.1.1.2}}`

- Utiliza DNS sobre HTTPS:

`doggo {{example.com}} @{{https://dns.quad9.net/dns-query}}`

- Salida en formato JSON:

`doggo {{example.com}} --json | jq '{{.responses[0].answers[].address}}'`

- Realiza una búsqueda DNS inversa:

`doggo --reverse {{8.8.4.4}} --short`
