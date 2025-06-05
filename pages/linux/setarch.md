# setarch

> Change the reported architecture for a program's execution, primarily used to modify how programs behave based on system architecture.
> Useful for compatibility testing or running legacy applications.
> More information: <https://manned.org/setarch.8>.

- Run a command as if the machine architecture is `i686` (useful for running 32-bit apps on a 64-bit kernel):

`setarch i686 {{command}}`

- Run a shell with the `x86_64` architecture:

`setarch x86_64 {{bash}}`

- Disable randomization of the virtual address space:

`setarch {{linux32}} {{[-R|--addr-no-randomize]}} {{command}}`

- List supported architectures:

`setarch --list`

- Display help:

`setarch {{[-h|--help]}}`
