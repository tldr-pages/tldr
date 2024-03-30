# speedread

> A simple terminal-based open source Spritz-alike.
> Shows input text as a per-word RSVP (rapid serial visual presentation) aligned on optimal reading points, which allows reading text at a much more rapid pace than usual as the eye can stay fixed on a single place.
> More information: <https://github.com/pasky/speedread>.

- Read a text file at a specific speed:

`cat {{path/to/file.txt}} | speedread -wpm {{250}}`

- Resume from a specific line:

`cat {{path/to/file.txt}} | speedread -resume {{5}}`

- Show multiple words at a time:

`cat {{path/to/file.txt}} | speedread -multiword`

- Slow down by 10% during the reading session:

`[`

- Speed up by 10% during the reading session:

`]`

- Pause, and show the last few lines as context:

`<space>`
