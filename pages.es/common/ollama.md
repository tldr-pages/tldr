# ollama

> Un ejecutor de modelos de lenguaje grande.
> Para ver una lista de los modelos disponibles, consulta <https://ollama.com/library>.
> Más información: <https://github.com/ollama/ollama>.

- Iniciar el demonio requerido para ejecutar otros comandos:

`ollama serve`

- Ejecutar un modelo y chatear con él:

`ollama run {{modelo}}`

- Ejecutar un modelo con un solo mensaje:

`ollama run {{modelo}} {{mensaje}}`

- Listar los modelos descargados:

`ollama list`

- Descargar/Actualizar un modelo específico:

`ollama pull {{modelo}}`

- Listar los modelos en ejecución:

`ollama ps`

- Eliminar un modelo:

`ollama rm {{modelo}}`

- Crear un modelo desde un `Modelfile` ([f]):

`ollama create {{nombre_nuevo_modelo}} -f {{ruta/al/Modelfile}}`
