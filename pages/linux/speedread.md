# speedread

> A Spritz-alike speed reader.
> Show text using per-word Rapid Serial Visual Presentation (RSVP).
> More information: <https://github.com/pasky/speedread>.

- Read a text file at a specific speed:

`cat {{path/to/file.txt}} | speedread -wpm {{250}}`

- Resume from a specific line:

`cat {{path/to/file.txt}} | speedread -resume {{5}}`

- Show multiple words at a time:

`cat {{path/to/file.txt}} | speedread -multiword`

- Slow down by 10% during the reading session:

`<[>`

- Speed up by 10% during the reading session:

`<]>`

- Pause, and show the last few lines as context:

`<Space>`
