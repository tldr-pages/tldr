# ollama

> Un ejecutor de modelos de lenguaje grande.
> Para ver una lista de los modelos disponibles, consulta <https://ollama.com/library>.
> Más información: <https://github.com/ollama/ollama>.

- Inicia el demonio requerido para ejecutar otros comandos:

`ollama serve`

- Ejecuta un modelo y chatea con él:

`ollama run {{modelo}}`

- Ejecuta un modelo con un solo mensaje:

`ollama run {{modelo}} {{mensaje}}`

- Lista los modelos descargados:

`ollama list`

- Descargar/Actualizar un modelo específico:

`ollama pull {{modelo}}`

- Listar los modelos en ejecución:

`ollama ps`

- Eliminar un modelo:

`ollama rm {{modelo}}`

- Crear un modelo desde un `Modelfile` ([f]):

`ollama create {{nombre_nuevo_modelo}} -f {{ruta/al/Modelfile}}`
