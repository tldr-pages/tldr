# dnsx

> Un paquete de herramientas DNS rápido y polivalente para ejecutar múltiples consultas DNS.
> Nota: En algunos casos, la entrada a `dnsx` debe pasarse a través de `stdin` ( pipe `|`).
> Vea también: `dig`, `dog`, `dnstracer`.
> Más información: <https://docs.projectdiscovery.io/opensource/dnsx/usage>.

- Consulta el registro A de un (sub)dominio y muestra la respuesta recibida:

`echo {{example.com}} | dnsx -a {{[-re|-resp]}}`

- Consulta todos los registros DNS (A, AAAA, CNAME, NS, TXT, SRV, PTR, MX, SOA, AXFR, CAA):

`dnsx <<< {{example.com}} -recon {{[-re|-resp]}}`

- Consulta un tipo específico de registro DNS:

`echo {{example.com}} | dnsx {{[-re|-resp]}} -{{a|aaaa|cname|ns|txt|srv|ptr|mx|soa|any|axfr|caa}}`

- Muestra solo la respuesta (sin mostrar el dominio o subdominio consultado):

`echo {{example.com}} | dnsx {{[-ro|-resp-only]}}`

- Muestra la respuesta sin procesar de una consulta, especificando los resolutores que se van a utilizar y los intentos de reintento en caso de fallos:

`echo {{example.com}} | dnsx -{{debug|raw}} {{[-r|-resolver]}} {{1.1.1.1,8.8.8.8,...}} -retry {{número}}`

- Ataque de fuerza bruta a registros DNS utilizando un marcador de posición:

`dnsx {{[-d|-domain]}} {{FUZZ.example.com}} {{[-w|-wordlist]}} {{ruta/a/wordlist.txt}} {{[-re|-resp]}}`

- Utiliza fuerza bruta en los registros DNS a partir de una lista de dominios y listas de palabras, añadiendo la salida a un archivo sin códigos de color:

`dnsx {{[-d|-domain]}} {{ruta/a/dominio.txt}} {{[-w|-wordlist]}} {{ruta/a/lista_de_palabras.txt}} {{[-re|-resp]}} {{[-o|-output]}} {{ruta/a/salida.txt}} {{[-nc|-no-color]}}`

- Extrae registros `CNAME` para la lista dada de subdominios, con limitación de la tasa de consultas DNS por segundo:

`subfinder -silent {{[-d|-domain]}} {{example.com}} | dnsx -cname {{[-re|-resp]}} {{[-rl|-rate-limit]}} {{number}}`
