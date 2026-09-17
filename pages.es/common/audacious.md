# audacious

> Un reproductor de audio de código abierto. Basado indirectamente en XMMS.
> Vea también: `audtool`, `clementine`, `mpc`, `ncmpcpp`.
> Más información: <https://manned.org/audacious>.

- Inicia la interfaz gráfica de usuario:

`audacious`

- Inicia una nueva instancia y reproducir un archivo de audio:

`audacious {{[-N|--new-instance]}} {{ruta/al/audio}}`

- Añade a la cola un directorio específico de archivos de audio:

`audacious {{[-e|--enqueue]}} {{ruta/al/directorio}}`

- Inicia o detiene la reproducción:

`audacious {{[-t|--play-pause]}}`

- Avanza ([fwd]) o retrocede ([rew]) en la lista de reproducción:

`audacious --{{fwd|rew}}`

- Detiene la reproducción:

`audacious {{[-s|--stop]}}`

- Inicia en modo CLI (sin interfaz gráfica):

`audacious {{[-H|--headless]}}`

- Sale tan pronto como se detenga la reproducción o no haya nada que reproducir:

`audacious {{[-q|--quit-after-play]}}`
