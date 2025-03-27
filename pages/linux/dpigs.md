# dpigs

> Show which installed packages occupy the most space on `apt` based systems.
> More information: <https://manned.org/dpigs>.

- Display the `n` largest packages on the system:

`dpigs {{[-n|--lines]}} {{n}}`

- Use the specified file instead of the default dpkg status file:

`dpigs {{[-s|--status]}} {{path/to/file}}`

- Display the largest source packages of binary packages installed on the system:

`dpigs {{[-S|--source]}}`

- Display package sizes in human-readable format:

`dpigs {{[-H|--human-readable]}}`

- Display help:

`dpigs {{[-h|--help]}}`
