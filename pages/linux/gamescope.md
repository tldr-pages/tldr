# gamescope

> A micro-compositor used as a game layer.
> More information: <https://github.com/ValveSoftware/gamescope>.

- Run a program with gamescope on the terminal:

`gamescope -- {{program}}`

- Run a game with gamescope through Steam:

`gamescope -- %command%`

- Upscale a 720p game to 1440p with integer scaling:

`gamescope {{[-h|--nested-height]}} 720 {{[-H|--output-height]}} 1440 {{[-S|--scaler]}} integer -- %command%`

- Limit a vsynced game to 30 FPS:

`gamescope {{[-r|--nested-refresh]}} 30 -- %command%`

- Toggle fullscreen:

`<Super f>`

- Show help:

`gamescope --help`
