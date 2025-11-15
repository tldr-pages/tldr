# asciinema

> Record and replay terminal sessions, and optionally share them on <https://asciinema.org>.
> See also: `terminalizer`.
> More information: <https://docs.asciinema.org/manual/cli/>.

- Associate the local install of `asciinema` with an asciinema.org account:

`asciinema {{[a|auth]}}`

- Make a new recording and save it to a local file (finish it with `<Ctrl d>` or type `exit`):

`asciinema {{[r|record]}} {{path/to/recording.cast}}`

- Replay a terminal recording from a local file:

`asciinema {{[p|play]}} {{path/to/recording.cast}}`

- Replay a terminal recording hosted on <https://asciinema.org>:

`asciinema {{[p|play]}} https://asciinema.org/a/{{cast_id}}`

- Make a new recording, limiting any idle time to at most 2.5 seconds:

`asciinema {{[r|record]}} {{[-i|--idle-time-limit]}} 2.5`

- Print the full output of a locally saved recording:

`asciinema {{[ca|cat]}} {{path/to/recording.cast}}`

- Upload a locally saved terminal session to asciinema.org:

`asciinema {{[u|upload]}} {{path/to/recording.cast}}`

- Stream the current terminal on a local webpage:

`asciinema {{[st|stream]}} --local`
