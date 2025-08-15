# dnsx

> Un equipo de herramientas de DNS rápido y multipropósito para ejecutar múltiples consultas DNS.
> Nota: la entrada a `dnsx` necesita ser pasada a través de `stdin` (tubería `|`) en algunos casos.
> Vea también: `dig`, `dog`, `dnstracer`.
> Más información: <https://docs.projectdiscovery.io/tools/dnsx/running>.

- Consulta el registro A de un (sub)dominio y muestra la [re]spuesta recibida:

`echo {{example.com}} | dnsx -a {{[-re|-resp]}}`

- Consulta todos los registros DNS (A, AAAA, CNAME, NS, TXT, SRV, PTR, MX, SOA, AXFR y CAA):

`dnsx -recon {{[-re|-resp]}} <<< {{example.com}}`

- Consulta un tipo específico de registro DNS:

`echo {{example.com}} | dnsx {{[-re|-resp]}} -{{a|aaaa|cname|ns|txt|srv|ptr|mx|soa|any|axfr|caa}}`

- Muestra solo la respuesta (no muestra el dominio o subdominio consultado):

`echo {{example.com}} | dnsx {{[-ro|-resp-only]}}`

- Muestra la respuesta sin procesar de una consulta, especificando los solucionadores a utilizar y el número de intentos en caso de haber errores:

`echo {{example.com}} | dnsx -{{debug|raw}} {{[-r|-resolver]}} {{1.1.1.1,8.8.8.8,...}} -retry {{número}}`

- Aplica fuerza bruta a los registros DNS utilizando un marcador de posición:

`dnsx {{[-d|-domain]}} {{FUZZ.example.com}} {{[-w|-wordlist]}} {{ruta/a/lista_de_palabras.txt}} {{[-re|-resp]}}`

- Aplica fuerza bruta a registros DNS a partir de una lista de dominios y listas de palabras, adjuntando la salida a un archivo sin códigos de color:

`dnsx {{[-d|-domain]}} {{ruta/a/dominio.txt}} {{[-w|-wordlist]}} {{ruta/a/lista_de_palabras.txt}} {{[-re|-resp]}} {{[-o|-output]}} {{ruta/a/salida.txt}} {{[-nc|-no-color]}}`

- Extrae registros `CNAME` desde una lista de subdominios, con una velocidad límite de consultas DNS por segundo:

`subfinder -silent {{[-d|-domain]}} {{example.com}} | dnsx -cname {{[-re|-resp]}} {{[-rl|-rate-limit]}} {{número}}`
