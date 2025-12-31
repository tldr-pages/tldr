# aider

> Programa de emparejamiento con el LLM de su elección.
> Más información: <https://github.com/Aider-AI/aider>.

- Inicia un nuevo proyecto o trabaja con una base de código existente:

`aider --model {{nombre_del_modelo}} --api-key {{su_clave_api}}`

- Añade nuevas funciones o casos de prueba a archivos específicos:

`aider {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Describe un error y deja que `aider` lo solucione:

`aider {{ruta/al/archivo}} --describe "{{descripción_de_un_fallo}}"`

- Refactoriza código en un archivo específico:

`aider {{ruta/al/archivo}} --refactor`

- Actualiza la documentación:

`aider {{ruta/al/archivo}} --update-docs`

- Muestra la ayuda:

`aider --help`
