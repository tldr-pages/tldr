# gifsicle

> Create GIFs.
> More information: <https://www.lcdf.org/gifsicle>.

- Optimise a GIF:

`gifsicle --batch --optimize=3 {{amin.gif}}`

- Make a GIF animation with gifsicle:

`gifsicle --delay={{10}} --loop *.gif > {{anim.gif}}`

- Extract frames from an animation:

`gifsicle {{anim.gif}} '#0' > {{firstframe.gif}}`

- You can also edit animations by replacing, deleting, or inserting frames:

`gifsicle -b {{anim.gif}} --replace '#0' {{new.gif}}`
