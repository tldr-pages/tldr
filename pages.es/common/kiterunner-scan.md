# kiterunner scan

> Un escáner web contextual para escanear simultáneamente rutas API y puntos finales web utilizando listas de palabras de kitebuilder.
> El subcomando `scan` se dirige a uno o varios hosts con solicitudes API estructuradas.
> Más información: <https://github.com/assetnote/kiterunner#usage>.

- Escanea un objetivo con una lista de palabras de Assetnote (por ejemplo, las primeras 5000 rutas de la API):

`kiterunner scan {{https://example.com}} {{[-A|--assetnote-wordlist]}} {{apiroutes-210228:5000}}`

- Analiza un objetivo con una lista de palabras de Kitebuilder:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{ruta/a/lista_de_palabras.kite}}`

- Analiza varios hosts desde un archivo con una lista de palabras de Kitebuilder:

`kiterunner scan {{ruta/a/hosts.txt}} {{[-w|--kitebuilder-list]}} {{ruta/a/lista_de_palabras.kite}}`

- Realiza un escaneo con una lista de palabras de Assetnote y salida en formato JSON:

`kiterunner scan {{https://example.com}} {{[-A|--assetnote-wordlist]}} {{apiroutes-210228:5000}} -o {{json}}`

- Realiza un escaneo con ajustes de concurrencia personalizados para mejorar el rendimiento:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{ruta/a/lista_de_palabras.kite}} {{[-x|--max-connection-per-host]}} {{5}} {{[-j|--max-parallel-hosts]}} {{100}}`

- Realiza un escaneo con una lista de palabras como si fuera una lista de palabras normal, desactivando el escaneo en profundidad:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{ruta/a/rafter.txt}} {{[-d|--preflight-depth]}} {{0}}`

- Realiza un escaneo con encabezados personalizados e ignora respuestas con una longitud de contenido específica:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{ruta/a/lista_de_palabras.kite}} {{[-H|--header]}} "{{Autorización: Token de portador}}" --ignore-length {{100-105}}`

- Realiza un escaneo completo con Kitebuilder sin escaneo por fases:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{ruta/a/lista_de_palabras.kite}} --kitebuilder-full-scan`
