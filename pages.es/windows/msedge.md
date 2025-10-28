# msedge

> Navegador web moderno desarrollado por Microsoft basado en el navegador web Chromium desarrollado por Google.
> Este comando está disponible como `microsoft-edge` en otras plataformas.
> Nota: Argumentos adicionales del comando de `chromium` también pueden ser utilizables para controlar Microsoft Edge.
> Más información: <https://microsoft.com/edge>.

- Abrir una URL o archivo específico:

`msedge {{https://example.com|ruta\al\archivo.html}}`

- Abrir en modo InPrivate:

`msedge --inprivate {{example.com}}`

- Abrir en una nueva ventana:

`msedge --new-window {{example.com}}`

- Abrir en modo aplicación (sin barras de herramientas, barra de URL, botones, etc.):

`msedge --app {{https://example.com}}`

- Usar un servidor proxy:

`msedge --proxy-server "{{socks5://hostname:66}}" {{example.com}}`

- Abrir con un directorio de perfil personalizado:

`msedge --user-data-dir {{ruta\al\directorio}}`

- Abrir sin validación CORS (útil para probar una API):

`msedge --user-data-dir {{ruta\al\directorio}} --disable-web-security`

- Abrir con una ventana de DevTools para cada pestaña abierta:

`msedge --auto-open-devtools-for-tabs`
