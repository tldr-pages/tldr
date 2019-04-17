# scriptreplay

> Output content of session files created by script command to standard output.

- Replay {{path/to/session.out}} at the speed it was recorded:

`scriptreplay {{path/to/timingfile}} {{path/to/session.out}}`

- Replay {{typescript_file}} at double-speed:

`scriptreplay {{path/to/timingfile}} {{path/to/session.out}} 2`

- Replay {{typescript_file}} at half-speed:

`scriptreplay {{path/to/timingfile}} {{path/to/session.out}} .5`
