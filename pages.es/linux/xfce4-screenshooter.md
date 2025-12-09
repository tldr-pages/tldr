# xfce4-screenshooter

> La herramienta de captura de pantalla de XFCE4.
> Más información: <https://docs.xfce.org/apps/xfce4-screenshooter/start>.

- Inicia la interfaz gráfica de usuario (GUI) de captura de pantalla:

`xfce4-screenshooter`

- Toma una captura de pantalla de toda la pantalla y lanza la GUI para preguntar cómo proceder:

`xfce4-screenshooter --fullscreen`

- Toma una captura de pantalla de toda la pantalla y la guarda en el directorio especificado:

`xfce4-screenshooter --fullscreen --save {{ruta/al/directorio}}`

- Espera un tiempo antes de tomar la captura de pantalla:

`xfce4-screenshooter --delay {{segundos}}`

- Toma una captura de pantalla de una región de la pantalla (selecciona usando el ratón):

`xfce4-screenshooter --region`

- Toma una captura de pantalla de la ventana activa, y la copia al portapapeles:

`xfce4-screenshooter --window --clipboard`

- Toma una captura de pantalla de la ventana activa, y la abre con un programa elegido:

`xfce4-screenshooter --window --open {{gimp}}`
