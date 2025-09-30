# wlc

> Gestiona proyectos de localización en una instancia de Weblate.
> Más información: <https://docs.weblate.org/en/latest/wlc.html#commands>.

- Lista los proyectos usando un archivo de configuración:

`wlc {{[-c|--config]}} {{ruta/al/archivo}} list-projects`

- Lista los componentes de un proyecto y anula la URL y la clave de la API:

`wlc {{[-u|--url]}} {{URL}} {{[-k|--key]}} {{clave}} ls {{proyecto}}`

- Lista las traducciones de un componente en un formato específico:

`wlc {{[-f|--format]}} {{text|csv|json|html}} ls {{proyecto}}/{{componente}}`

- Imprime las estadísticas de un proyecto:

`wlc stats {{proyecto}}`

- Muestra la ayuda:

`wlc {{[-h|--help]}}`
