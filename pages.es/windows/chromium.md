# chromium

> Navegador web de código abierto desarrollado y mantenido principalmente por Google.
> Nota: Es posible que necesites reemplazar el comando `chromium` con tu navegador web deseado, como `brave`, `google-chrome`, `microsoft-edge`/`msedge`, `opera` o `vivaldi`.
> Más información: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Abre una URL o archivo específico:

`chromium {{https://example.com|ruta\al\archivo.html}}`

- Abre en modo incógnito (usa `--inprivate` para Microsoft Edge):

`{{chromium --incognito|msedge --inprivate}} {{example.com}}`

- Abre en una nueva ventana:

`chromium --new-window {{example.com}}`

- Abre en modo aplicación (sin barras de herramientas, barra de URLs, botones, etc.):

`chromium --app {{https://example.com}}`

- Usa un servidor proxy:

`chromium --proxy-server "{{socks5://hostname:66}}" {{example.com}}`

- Abre con un directorio de perfil personalizado:

`chromium --user-data-dir {{ruta\al\directorio}}`

- Abre sin validación CORS (útil para probar una API):

`chromium --user-data-dir {{ruta\al\directorio}} --disable-web-security`

- Abre con una ventana de Desarrolador para cada pestaña abierta:

`chromium --auto-open-devtools-for-tabs`
