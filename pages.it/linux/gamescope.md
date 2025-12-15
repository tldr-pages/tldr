# gamescope

> Un micro-compositor utilizzato come livello di gioco.
> Vedi anche: `cage`.
> Maggiori informazioni: <https://github.com/ValveSoftware/gamescope#keyboard-shortcuts>.

- Esegui un programma con gamescope nel terminale:

`gamescope -- {{program}}`

- Esegui un gioco con gamescope tramite Steam:

`gamescope -- %command%`

- Upscala un gioco 720p a 1440p con integer scaling:

`gamescope {{[-h|--nested-height]}} 720 {{[-H|--output-height]}} 1440 {{[-S|--scaler]}} integer -- {{command}}`

- Limita un gioco con vsync a 30 FPS:

`gamescope {{[-r|--nested-refresh]}} 30 -- {{command}}`

- Avvia Steam in Big Picture Mode e integra con gamescope:

`gamescope {{[-e|--steam]}} -- /usr/bin/steam -tenfoot`

- Specifica quale display preferire:

`gamescope {{[-O|--prefer-output]}} {{HDMI-A-1,DP-3,...}} -- {{program}}`

- Attiva/disattiva schermo intero:

`<Super f>`

- Visualizza la guida:

`gamescope --help`
