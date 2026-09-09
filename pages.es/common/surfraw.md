# surfraw

> Realiza consultas en diversos motores de búsqueda web.
> Consiste en una colección de elvi, cada uno de los cuales sabe cómo realizar búsquedas en un sitio web.
> Más información: <https://manned.org/surfraw>.

- Muestra la lista de scripts de búsqueda en sitios web compatibles (elvi):

`surfraw -elvi`

- Abre en el navegador la página de resultados del elvi para una búsqueda específica:

`surfraw {{nombre_elvi}} "{{términos_búsqueda}}"`

- Mostrar la descripción de un elvi y sus opciones específicas:

`surfraw {{nombre_elvi}} {{[-lh|-local-help]}}`

- Realiza una búsqueda utilizando un elvi con opciones específicas y abrir la página de resultados en el navegador:

`surfraw {{nombre_elvi}} {{opciones_elvi}} "{{términos_búsqueda}}"`

- Muestra la URL de la página de resultados del elvi para una búsqueda concreta:

`surfraw -print {{nombre_elvi}} "{{términos_búsqueda}}"`

- Realiza una búsqueda utilizando el alias:

`sr {{nombre_elvi}} "{{términos_búsqueda}}"`
