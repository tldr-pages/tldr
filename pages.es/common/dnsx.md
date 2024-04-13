# dnsx

> Un equipo de herramientas de DNS rápido y multipropósito para ejecutar múltiples consultas DNS.
> Nota: la entrada a `dnsx` necesita ser pasada a través de `stdin` (tubería `|`) en algunos casos.
> Ver también: `dig`, `dog`, `dnstracer`.
> Más información: <https://github.com/projectdiscovery/dnsx>.

- Consulta el registro A de un subdominio y muestra la [re]spuesta recibida:

`echo {{ejemplo.com}} | dnsx -a -re`

- Consulta todos los registros DNS (A,AAAA,CNAME,NS,TXT,SRV,PTR,MX,SOA,AXFR,CAA):

`dnsx -recon -re <<< {{ejemplo.com}}`

- Consulta un tipo específico de registro DNS:

`echo {{ejemplo.com}} | dnsx -re -{{a|aaaa|cname|ns|txt|srv|ptr|mx|soa|any|axfr|caa}}`

- Muestra s[o]lo la [r]espuesta (no muestra el dominio o subdominio consultado):

`echo {{ejemplo.com}} | dnsx -ro`

- Muestra la respuesta sin procesar de una consulta, especificando los solucionado[r]es a utilizar y los intentos de reintentos en caso de error:

`echo {{ejemplo.com}} | dnsx -{{debug|raw}} -resolver {{1.1.1.1,8.8.8.8,...}} -retry {{número}}`

- Fuerza bruta de registros DNS utilizando un marcador de posición:

`dnsx -dominio {{FUZZ.ejemplo.com}} -wordlist {{ruta/a/lista_de_palabras.txt}} -re`

- Registros DNS de fuerza bruta a partir de una lista de [d]ominios y listas de palabras, adjuntando la salida [o] a un archivo sin códigos de [c]olor:

`dnsx -dominio {{ruta/a/dominio.txt}} -wordlist {{ruta/a/lista_palabras.txt}} -re -output {{ruta/a/salida.txt}} -no-color`

- Extrae registros `CNAME` desde la lista dada de subdominios, con una velocidad [l]imitante de consultas DNS por segundo:

`subfinder -silent -d {{ejemplo.com}} | dnsx -cname -re -rl {{número}}`
