# gifsicle

> Create gifs

- Making a GIF animation with gifsicle is easy:

`gifsicle --delay=10 --loop *.gif > anim.gif`

- Extracting frames from animations is easy too:

`gifsicle anim.gif '#0' > firstframe.gif`

- You can also edit animations by replacing, deleting, or inserting frames:

`gifsicle -b anim.gif --replace '#0' new.gif`
