# kiterunner brute

> Un escáner web contextual para realizar ataques de fuerza bruta en rutas de API y puntos finales web utilizando listas de palabras.
> El subcomando `brute` se dirige a uno o varios hosts.
> Más información: <https://github.com/assetnote/kiterunner#usage>.

- Realiza un ataque de fuerza bruta a un objetivo con una lista de palabras de Assetnote (por ejemplo, las primeras 20 000 rutas de API):

`kiterunner brute {{https://example.com}} {{[-A|--assetnote-wordlist]}} {{apiroutes-210328:20000}}`

- Realiza un ataque de fuerza bruta a un objetivo con una lista de palabras personalizada:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{ruta/a/lista_palabras.txt}}`

- Realiza un ataque de fuerza bruta utilizando una lista de palabras al estilo dirsearch con sustitución de extensiones:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{ruta/a/dirsearch.txt}} {{[-D|--dirsearch-compat]}} {{[-e|--extensions]}} {{json,txt}}`

- Ataque de fuerza bruta con extensiones de archivo específicas añadidas y salida en formato JSON:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{ruta/a/lista_palabras.txt}} {{[-e|--extensions]}} {{aspx,ashx}} {{[-o|--output]}} {{json}}`

- Ataque de fuerza bruta a una lista de objetivos desde un archivo con ajustes de concurrencia personalizados para mejorar el rendimiento:

`kiterunner brute {{ruta/a/objetivos.txt}} {{[-w|--wordlist]}} {{ruta/a/lista_palabras.txt}} {{[-x|--max-connection-per-host]}} {{5}} {{[-j|--max-parallel-hosts]}} {{100}}`

- Realiza un ataque de fuerza bruta e ignora respuestas con una longitud de contenido específica:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{ruta/a/lista_palabras.txt}} --ignore-length {{100-105}}`

- Ataque de fuerza bruta con encabezados HTTP personalizados:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{ruta/a/lista_palabras.txt}} {{[-H|--header]}} "{{Authorization: Bearer token}}"`

- Ataque de fuerza bruta a una lista de objetivos desde un archivo con filtrado de códigos de estado de error:

`kiterunner brute {{ruta/a/objetivos.txt}} {{[-w|--wordlist]}} {{ruta/a/lista_palabras.txt}} --fail-status-codes {{400,401,404}}`
