# audacious

> Un reproductor de audio de código abierto. Basado indirectamente en XMMS.
> Vea también: `audtool`, `clementine`, `mpc`, `ncmpcpp`.
> Más información: <https://manned.org/audacious>.

- Inicia la interfaz gráfica:

`audacious`

- Inicia una nueva instancia y reproduce un audio:

`audacious --new-instance {{ruta/al/audio}}`

- Pone en cola un directorio específico de archivos de audio:

`audacious --enqueue {{ruta/al/directorio}}`

- Inicia o detiene la reproducción:

`audacious --play-pause`

- Salta hacia delante ([fwd]) o hacia atrás ([rew]) en la lista de reproducción:

`audacious --{{fwd|rew}}`

- Detiene la reproducción:

`audacious --stop`

- Inicia en modo CLI (headless):

`audacious --headless`

- Sale en cuanto se detenga la reproducción o no haya nada que reproducir:

`audacious --quit-after-play`
