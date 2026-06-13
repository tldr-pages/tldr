# dog

> Utilidad de búsqueda DNS.
> Tiene una salida colorida, es compatible con los protocolos DNS sobre TLS y DNS sobre https, y puede emitir JSON.
> Más información: <https://github.com/ogham/dog#examples>.

- Busca las direcciones IP asociadas a un nombre de host (registros A):

`dog {{example.com}}`

- Consulta el tipo de registros MX asociados a un nombre de dominio determinado:

`dog {{example.com}} MX`

- Especifica un servidor DNS concreto para la consulta (por ejemplo, Cloudflare):

`dog {{example.com}} MX @{{1.1.1.1}}`

- Consulta a través de TCP en lugar de UDP:

`dog {{example.com}} MX @{{1.1.1.1}} {{[-T|--tcp]}}`

- Consulta el tipo de registros MX asociados a un nombre de dominio determinado a través de TCP utilizando argumentos explícitos:

`dog {{[-q|--query]}} {{example.com}} {{[-t|--type]}} MX {{[-n|--nameserver]}} {{1.1.1.1}} {{[-T|--tcp]}}`

- Busca las direcciones IP asociadas a un nombre de host (registros A) utilizando DNS sobre https (DoH):

`dog {{example.com}} {{[-H|--https]}} @{{https://cloudflare-dns.com/dns-query}}`
