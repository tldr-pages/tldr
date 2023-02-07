# arch

> Display the name of the system architecture, or run a command under a different architecture.
> See also `uname`.
> More information: <https://www.unix.com/man-page/osx/1/arch/>.

- Display the system's architecture:

`arch`

- Run a command using x86_64:

`arch -x86_64 "{{command}}"`

- Run a command using arm:

`arch -arm64 "{{command}}"`
