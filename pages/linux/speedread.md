# speedread

> A simple terminal-based open source Spritz-alike.
> This command line filter shows input text as a per-word RSVP (rapid serial visual presentation) aligned on optimal reading points.
> This kind of input mode allows reading text at a much more rapid pace than usual as the eye can stay fixed on a single place.
>
> More information: <https://github.com/pasky/speedread>

- Basic example.  Read `tea.txt` at a speed of 250 wpm:

`cat tea.txt | speedread -wpm 250`

- Resume from line:

`cat tea.txt | speedread -resume 5`

- Show multiple words at a time:

`cat tea.txt | speedread -multiword`

- Controls:
> [        slow down by 10%
> ]        speed up by 10%
> space    pause, and show the last few lines as context

