# kiterunner kb

> Un escáner web contextual para manipular esquemas de KiteBuilder utilizados en el descubrimiento de API y puntos finales web.
> El subcomando `kb` se encarga de la compilación, conversión, análisis y reproducción de solicitudes de esquemas.
> Más información: <https://github.com/assetnote/kiterunner#usage>.

- Compila un esquema de KiteBuilder desde JSON a un archivo Kite:

`kiterunner kb compile {{ruta/a/lista_de_palabras.json}} {{ruta/a/lista_de_palabras.kite}}`

- Convierte un archivo Kite en una lista de palabras de texto:

`kiterunner kb convert {{ruta/a/lista_de_palabras.kite}} {{ruta/a/lista_de_palabras.txt}}`

- Convierte una lista de palabras en formato de texto a un archivo Kite:

`kiterunner kb convert {{ruta/a/lista_de_palabras.txt}} {{ruta/a/lista_de_palabras.kite}}`

- Convierte un archivo Kite a un esquema JSON:

`kiterunner kb convert {{ruta/a/lista_de_palabras.kite}} {{ruta/a/lista_de_palabras.json}}`

- Analiza un esquema de KiteBuilder y generar datos JSON formateados:

`kiterunner kb parse {{ruta/a/lista_de_palabras.json}} {{[-o|--output]}} {{json}}`

- Analiza un archivo Kite y genera datos de texto formateados:

`kiterunner kb parse {{ruta/a/lista_de_palabras.kite}} {{[-o|--output]}} {{texto}}`

- Reproduce una solicitud específica a partir de la salida de un esquema de KiteBuilder:

`kiterunner kb replay {{[-w|--kitebuilder-list]}} {{ruta/a/lista_de_palabras.kite}} "{{solicitud_salida}}"`

- Reproduce una solicitud a través de un proxy para su inspección:

`kiterunner kb replay {{[-w|--kitebuilder-list]}} {{ruta/a/lista_de_palabras.kite}} {{[-p|--proxy]}} {{http://localhost:8080}} "{{solicitud_salida}}"`
