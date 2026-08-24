# fakeroot

> Run a command in an environment faking root privileges for file manipulation.
> More information: <https://manned.org/fakeroot>.

- Start the default shell as fakeroot:

`fakeroot`

- Run a command as fakeroot:

`fakeroot -- {{command}} {{command_arguments}}`

- Run a command as fakeroot and [s]ave the environment to a file on exit:

`fakeroot -s {{path/to/file}} -- {{command}} {{command_arguments}}`

- Load a fakeroot environment and run a command as fakeroot:

`fakeroot -i {{path/to/file}} -- {{command}} {{command_arguments}}`

- Run a command keeping the real ownership of files instead of pretending they are owned by root:

`fakeroot {{[-u|--unknown-is-real]}} -- {{command}} {{command_arguments}}`

- Display help:

`fakeroot {{[-h|--help]}}`
