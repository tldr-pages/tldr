# gamescope

> A micro-compositor used as a game layer.
> See also: `cage`.
> More information: <https://github.com/ValveSoftware/gamescope>.

- Run a program with gamescope on the terminal:

`gamescope -- {{program}}`

- Run a game with gamescope through Steam:

`gamescope -- %command%`

- Upscale a 720p game to 1440p with integer scaling:

`gamescope {{[-h|--nested-height]}} 720 {{[-H|--output-height]}} 1440 {{[-S|--scaler]}} integer -- %command%`

- Limit a vsynced game to 30 FPS:

`gamescope {{[-r|--nested-refresh]}} 30 -- %command%`

- Launch Steam in Big Picture Mode and integrate with gamescope:

`gamescope {{[-e|--steam]}} -- /usr/bin/steam -tenfoot`

- Specify which display to prefer:

`gamescope {{[-O|--prefer-output]}} {{HDMI-A-1,DP-3,...}} -- {{program}}`

- Toggle fullscreen:

`<Super f>`

- Display help:

`gamescope --help`
