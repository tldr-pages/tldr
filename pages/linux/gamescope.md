# gamescope

> Micro-compositor used as a game layer.
> More information: <https://github.com/ValveSoftware/gamescope>

- Upscale a 720p game to 1440p with integer scaling:

`gamescope -h 720 -H 1440 -S integer -- %command%`

- Limit a vsynced game to 30 FPS

`gamescope -r 30 -- %command%`

- Get a full list of options:

`gamescope --help`
