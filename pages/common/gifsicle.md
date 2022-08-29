# gifsicle

> GIF manipulator.
> More information: <https://www.lcdf.org/gifsicle>.

- Optimize a GIF as a new file:

`gifsicle {{path/to/input.gif}} --optimize=3 -o {{path/to/output.gif}}`

- Unoptimize a GIF in place:

`gifsicle -b {{path/to/input.gif}} --unoptimize`

- Extract a frame from a GIF:

`gifsicle {{path/to/input.gif}} '#{{0}}' > {{path/to/firstframe.gif}}`

- Make a GIF animation from selected GIFs:

`gifsicle {{*.gif}} --delay={{10}} --loop > {{path/to/output.gif}}`

- Reduce file size using lossy compression:

`gifsicle -b {{path/to/input.gif}} --optimize=3 --lossy={{100}} --colors={{16}} --dither`

- Delete the first 10 frames and all frames after frame 20 from a GIF:

`gifsicle -b {{path/to/input.gif}} --delete '#{{0-9}}' '#{{20-}}'`

- Modify all frames of a GIF using specific transformation options:

`gifsicle -b --crop {{50}},{{50}}+{{-50}}x{{-50}} --scale {{0.25}} --flip-horizontal --rotate-90 {{path/to/input.gif}}`
