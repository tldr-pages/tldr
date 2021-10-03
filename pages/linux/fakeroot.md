# fakeroot

> Run a command in an environment faking root privileges for file manipulation.
> More information: <https://manpages.debian.org/latest/fakeroot/fakeroot.1.html>.

- Start the default shell as fakeroot:

`fakeroot`

- Run a command as fakeroot:

`fakeroot -- {{command}} {{command_arguments}}`

- Run a command as fakeroot and save the environment to a file on exit:

`fakeroot -s {{path/to/file}} -- {{command}} {{command_arguments}}`

- Load a fakeroot environment and run a command as fakeroot:

`fakeroot -i {{path/to/file}} -- {{command}} {{command_arguments}}`

- Run a command keeping the real ownership of files instead of pretending they are owned by root:

`fakeroot --unknown-is-real -- {{command}} {{command_arguments}}`

- Display help:

`fakeroot --help`
