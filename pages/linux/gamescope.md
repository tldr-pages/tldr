# gamescope

> Micro-compositor used as a game layer.
> More information: <https://github.com/ValveSoftware/gamescope>.

- Run a program with gamescope:

`gamescope -- {{command}}`

- Upscale a 720p game to 1440p with integer scaling:

`gamescope {{[-h|--nested-height]}} 720 {{[-H|--output-height]}} 1440 {{[-S|--scaler]}} integer -- %command%`

- Limit a vsynced game to 30 FPS:

`gamescope {{[-r|--nested-refresh]}} 30 -- %command%`

- Get a full list of options:

`gamescope --help`
