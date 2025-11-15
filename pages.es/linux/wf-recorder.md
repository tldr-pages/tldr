# wf-recorder

> Screencast para Wayland opcionalmente con audio.
> Por defecto necesita terminar el proceso con `<Ctrl c>`.
> Más información: <https://github.com/ammen99/wf-recorder>.

- Grabación de un archivo MP4:

`wf-recorder --file={{salida.mp4}}`

- Graba video incluyendo audio; y esto incluye acceso al micrófono y los sonidos del sistema:

`wf-recorder --audio --file={{/ruta/al/archivo_con_audio.webm}}`

- Selecciona y graba una porción de la pantalla utilizando `slurp`, guardando en `recording.mp4` de forma predeterminada:

`wf-recorder -g "$(slurp)"`
