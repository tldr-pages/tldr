# speedread

> A simple terminal-based open source Spritz-alike.
> Shows input text as a per-word RSVP (rapid serial visual presentation) aligned on optimal reading points, which allows reading text at a much more rapid pace than usual as the eye can stay fixed on a single place.
> More information: <https://github.com/pasky/speedread>.

- Read a text file at a specific speed:

`speedread -wpm {{250}} < {{path/to/file.txt}}`

- Resume from a specific line:

`speedread -resume {{5}} < {{path/to/file.txt}}`

- Show multiple words at a time:

`speedread -multiword < {{path/to/file.txt}}`

- Slow down by 10% during the reading session:

`<[>`

- Speed up by 10% during the reading session:

`<]>`

- Pause, and show the last few lines as context:

`<Space>`
