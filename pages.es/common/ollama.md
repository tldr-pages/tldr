# ollama

> Un programa para ejecutar modelos de lenguaje grandes.
> Para ver una lista de los modelos disponibles, vea <https://ollama.com/library>.
> Más información: <https://docs.ollama.com/cli>.

- Inicia el programa residente necesario para ejecutar otros comandos:

`ollama serve`

- Ejecuta un modelo y chatea con él:

`ollama run {{modelo}}`

- Ejecuta un modelo con una sola indicación y el pensamiento desactivado:

`ollama run {{modelo}} --think=false "{{indicación}"`

- Enumera los modelos descargados:

`ollama {{[ls|list]}}`

- Extrae un modelo específico:

`ollama pull {{modelo}}`

- Lista los modelos en ejecución:

`ollama ps`

- Elimina un modelo:

`ollama rm {{modelo}}`

- Crea un modelo a partir de un `Modelfile`:

`ollama create {{nombre_del_nuevo_modelo}} {{[-f|--file]}} {{ruta/al/Modelfile}}`
