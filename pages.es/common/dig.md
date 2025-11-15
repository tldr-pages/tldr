# dig

> Utilidad de búsqueda DNS.
> Más información: <https://manned.org/dig>.

- Busca la(s) IP(s) asociada(s) a un nombre de host (registros A):

`dig +short {{example.com}}`

- Muestra una respuesta detallada para un dominio dado (registros A):

`dig +noall +answer {{example.com}}`

- Consulta un tipo de registro DNS específico asociado a un nombre de dominio determinado:

`dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}`

- Especifica un servidor DNS alternativo para consultar y, opcionalmente, utiliza DNS sobre TLS (DoT):

`dig {{+tls}} @{{1.1.1.1|8.8.8.8|9.9.9.9|...}} {{example.com}}`

- Realiza una búsqueda DNS inversa en una dirección IP (registro PTR):

`dig -x {{8.8.8.8}}`

- Busca servidores de nombres autoritativos para la zona y muestra los registros SOA:

`dig +nssearch {{example.com}}`

- Realiza consultas iterativas y muestra la ruta de rastreo completa para resolver un nombre de dominio:

`dig +trace {{example.com}}`

- Consulta un servidor DNS a través de un [p]uerto no estándar utilizando el protocolo TCP:

`dig +tcp -p {{puerto}} @{{dns_servidor_ip}} {{example.com}}`
