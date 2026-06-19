# viddy

> A modern `watch` command.
> More information: <https://github.com/sachaos/viddy>.

- Run a command repeatedly:

`viddy {{command}}`

- Run a command at a specific interval:

`viddy {{[-n|--interval]}} {{5s}} {{command}}`

- Highlight differences between updates:

`viddy {{[-d|--differences]}} {{command}}`

- Ring the terminal bell when output changes:

`viddy {{[-b|--bell]}} {{command}}`

- Run a command directly instead of through `sh -c`:

`viddy {{[-x|--exec]}} {{command}} {{arg1 arg2 ...}}`

- Display help:

`viddy {{[-h|--help]}}`

- Display version:

`viddy {{[-V|--version]}}`
