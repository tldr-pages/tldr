# firefox

> Un navegador web gratuito y de código abierto.
> Más información: <https://wiki.mozilla.org/Firefox/CommandLineOptions>.

- Inicia Firefox y abre una página web:

`firefox {{https://www.duckduckgo.com}}`

- Abre una nueva ventana:

`firefox --new-window {{https://www.duckduckgo.com}}`

- Abre una ventana privada (incógnito):

`firefox --private-window`

- Busca "wikipedia" utilizando el motor de búsqueda predeterminado:

`firefox --search "{{wikipedia}}"`

- Inicia Firefox en modo seguro, con todas las extensiones desactivadas:

`firefox --safe-mode`

- Hace una captura de pantalla de una página web en modo sin interfaz gráfica:

`firefox --headless --screenshot {{ruta/al/archivo_de_salida.png}} {{https://example.com/}}`

- Utiliza un perfil específico para permitir que se ejecuten varias instancias independientes de Firefox a la vez:

`firefox --profile {{ruta/al/directorio}} {{https://example.com/}}`

- Establece Firefox como navegador predeterminado:

`firefox --setDefaultBrowser`
