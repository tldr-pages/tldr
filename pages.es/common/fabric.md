# fabric

> Un marco de código abierto para mejorar las capacidades humanas mediante la IA.
> Proporciona un marco modular para resolver problemas específicos utilizando un conjunto de indicaciones de IA obtenidas mediante crowdsourcing.
> Más información: <https://github.com/danielmiessler/fabric#usage>.

- Ejecuta la instalación para configurar fabric:

`fabric {{[-S|--setup]}}`

- Muestra todos los patrones disponibles:

`fabric {{[-l|--listpatterns]}}`

- Ejecuta un patrón con la entrada de un archivo:

`fabric {{[-p|--pattern]}} {{nombre_del_patrón}} < {{ruta/a/archivo_de_entrada}}`

- Ejecuta un patrón en una dirección URL de YouTube:

`fabric {{[-y|--youtube]}} "{{https://www.youtube.com/watch?v=video_id}}" {{[-p|--pattern]}} {{nombre_del_patrón}}`

- Encadena patrones conectando la salida de uno al otro:

`fabric {{[-p|--pattern]}} {{pattern1}} | fabric {{[-p|--pattern]}} {{pattern2}}`

- Ejecuta un patrón personalizado definido por el usuario:

`fabric {{[-p|--pattern]}} {{nombre_patrón_personalizado}}`

- Ejecuta un patrón y guarda la salida en un archivo:

`fabric {{[-p|--pattern]}} {{nombre_del_patrón}} {{[-o|--output]}} {{ruta/al/archivo_de_salida}}`

- Ejecuta un patrón con las variables especificadas:

`fabric {{[-p|--pattern]}} {{nombre_del_patrón}} {{[-v|--variable]}} "{{nombre_variable}}:{{valor}}"`
