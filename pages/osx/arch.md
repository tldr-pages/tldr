# arch

> Display the name of the system architecture, or run a command under a different architecture.
> See also: `uname`.
> More information: <https://keith.github.io/xcode-man-pages/arch.1.html>.

- Display the system's architecture:

`arch`

- Run a command using x86_64:

`arch -x86_64 {{command}} {{argument1 argument2 ...}}`

- Run a command using ARM:

`arch -arm64 {{command}} {{argument1 argument2 ...}}`
