# orca-c

> A C-port of the ORCA live programming environment.
> ORCA is an esoteric programming language for creating procedural sequencers.
> More information: <https://github.com/hundredrabbits/Orca-c>.

- Start ORCA with an empty workspace:

`orca-c`

- Start ORCA and open a specific file:

`orca-c {{path/to/file.orca}}`

- Start ORCA and set a specific tempo (defaults to 120):

`orca-c --bpm {{beats_per_minute}}`

- Start ORCA and set the size of the grid:

`orca-c --initial-size {{columns}}x{{rows}}`

- Start ORCA and set the maximum number of undo steps (defaults to 100):

`orca-c --undo-limit {{limit}}`

- Show the main menu inside of ORCA:

`F1`

- Show all shortcuts inside of ORCA:

`?`

- Show all ORCA operators inside of ORCA:

`<Ctrl> + g`
