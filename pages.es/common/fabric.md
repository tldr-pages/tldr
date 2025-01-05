# fabric

> Un marco de trabajo de código abierto para aumentar el número de humanos utilizando IA.
> Proporciona un marco modular para resolver problemas específicos utilizando un conjunto de instrucciones de IA de origen colectivo.
> Más información: <https://github.com/danielmiessler/fabric>.

- Ejecuta el setup para configurar fabric:

`fabric --setup`

- Lista todos los patrones disponibles:

`fabric --listpatterns`

- Ejecuta un patrón con la entrada de un archivo:

`fabric --pattern {{nombre_del_patrón}} < {{ruta/al/archivo_de_entrada}}`

- Ejecuta un patrón en la URL de un vídeo de YouTube:

`fabric --youtube "{{https://www.youtube.com/watch?v=id_del_video}}" --pattern {{nombre_del_patrón}}`

- Encadena patrones pasando la salida de uno a otro:

`fabric --pattern {{patrón1}} | fabric --pattern {{patrón2}}`

- Ejecuta un patrón personalizado definido por el usuario:

`fabric --pattern {{nombre_patrón_personalizado}}`

- Ejecuta un patrón y guarda el resultado en un archivo:

`fabric --pattern {{nombre_del_patrón}} --output {{ruta/a/archivo_salida}}`

- Ejecuta un patrón con las variables especificadas:

`fabric --pattern {{nombre_del_patrón}} --variable "{{nombre_de_la_variable}}:{{valor}}"`
