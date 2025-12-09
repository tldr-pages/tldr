# kcat

> Productor Apache Kafka y herramienta de consumo.
> Más información: <https://github.com/edenhill/kcat>.

- Consume mensajes empezando por el corrimiento (offset) más nuevo:

`kcat -C -t {{tema}} -b {{intermediarios}}`

- Consume mensajes comenzando con el offset más antiguo y sale después de recibir el último mensaje:

`kcat -C -t {{tema}} -b {{intermediarios}} -o beginning -e`

- Consume mensajes como grupo de consumidores de Kafka:

`kcat -G {{id_de_grupo}} {{tema}} -b {{intermediarios}}`

- Publica el mensaje leyendo de `stdin`:

`echo {{mensaje}} | kcat -P -t {{tema}} -b {{intermediarios}}`

- Publica mensajes leyendo desde un archivo:

`kcat -P -t {{tema}} -b {{intermediarios}} {{ruta/al/archivo}}`

- Lista metadatos para todos los temas e intermediarios:

`kcat -L -b {{intermediarios}}`

- Lista metadatos para un tema específico:

`kcat -L -t {{tema}} -b {{intermediarios}}`

- Obtiene el offset de un tema/partición para un punto específico en el tiempo:

`kcat -Q -t {{tema}}:{{partición}}:{{marca_de_tiempo_unix}} -b {{intermediarios}}`
