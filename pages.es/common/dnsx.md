# dnsx

> Un equipo de herramientas de DNS rápido y multipropósito para ejecutar múltiples consultas DNS.
> Nota: la entrada a `dnsx` necesita ser pasada a través de `stdin` (tubería `|`) en algunos casos.
> Ver también: `dig`, `dog`, `dnstracer`.
> Más información: <https://github.com/projectdiscovery/dnsx>.

- Consulta el registro A de un subdominio y muestra la [re]spuesta recibida:

`echo {{ejemplo.com}} | dnsx -a -re`

- Consulta todos los registros DNS (A, AAAA, CNAME, NS, TXT, SRV, PTR, MX, SOA, AXFR y CAA):

`dnsx -recon -re <<< {{ejemplo.com}}`

- Consulta un tipo específico de registro DNS:

`echo {{ejemplo.com}} | dnsx -re -{{a|aaaa|cname|ns|txt|srv|ptr|mx|soa|any|axfr|caa}}`

- Muestra s[o]lo la [r]espuesta (no muestra el dominio o subdominio consultado):

`echo {{ejemplo.com}} | dnsx -ro`

- Muestra la respuesta sin procesar una consulta, especificando los solucionado[r]es a utilizar y el número de intentos en caso de haber errores:

`echo {{ejemplo.com}} | dnsx -{{debug|raw}} -resolver {{1.1.1.1,8.8.8.8,...}} -retry {{número}}`

- Aplica fuerza bruta a registros DNS utilizando un marcador de posición:

`dnsx -domain {{FUZZ.ejemplo.com}} -wordlist {{ruta/a/lista_de_palabras.txt}} -re`

- Aplica fuerza bruta a registros DNS a partir de una lista de [d]ominios y listas de palabras, adjuntando la salida a un archivo sin códigos de [c]olor:

`dnsx -domain {{ruta/a/dominio.txt}} -wordlist {{ruta/a/lista_de_palabras.txt}} -re -output {{ruta/a/salida.txt}} -no-color`

- Extrae registros `CNAME` desde una lista de subdominios, con una velocidad [l]ímite de consultas DNS por segundo:

`subfinder -silent -d {{ejemplo.com}} | dnsx -cname -re -rl {{número}}`
