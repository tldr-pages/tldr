# flatpak

> Construye, instala y ejecuta aplicaciones y tiempos de ejecución flatpak.
> Más información: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- Ejecuta una aplicación instalada:

`flatpak run {{com.example.app}}`

- Instala una aplicación desde una fuente remota:

`flatpak install {{nombre_remoto}} {{com.example.app}}`

- Lista las aplicaciones instaladas, ignorando los tiempos de ejecución:

`flatpak list --app`

- Actualiza todas las aplicaciones y tiempos de ejecución instalados:

`flatpak update`

- Añade una fuente remota:

`flatpak remote-add --if-not-exists {{nombre_remoto}} {{url_remota}}`

- Elimina una aplicación instalada:

`flatpak remove {{com.example.app}}`

- Elimina todas las aplicaciones no utilizadas:

`flatpak remove --unused`

- Muestra información sobre una aplicación instalada:

`flatpak info {{com.example.app}}`
