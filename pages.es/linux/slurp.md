# slurp

> Selecciona una región en un compositor Wayland.
> Más información: <https://github.com/emersion/slurp/blob/master/slurp.1.scd>.

- Selecciona una región y la imprime en `stdout`:

`slurp`

- Selecciona una región e imprímela en `stdout`, mientras muestras las dimensiones de la selección:

`slurp -d`

- Selecciona un único punto en lugar de una región:

`slurp -p`

- Selecciona una salida e imprime su nombre:

`slurp -o -f '%o'`

- Selecciona una región determinada y hace una captura de pantalla sin bordes utilizando `grim`:

`grim -g "$(slurp -w 0)"`

- Selecciona una región determinada y graba un vídeo sin bordes utilizando `wf-recorder`:

`wf-recorder --geometry "$(slurp -w 0)"`
