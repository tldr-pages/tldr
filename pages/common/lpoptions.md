# lpoptions

> Display or set printer options and defaults.
> See also: `lpadmin`.
> More information: <https://www.cups.org/doc/man-lpoptions.html>.

- Set the default printer:

`lpoptions -d {{printer[/instance]}}`

- [l]ist printer-specific options of a specific printer:

`lpoptions -d {{printer}} -l`

- Set a new [o]ption on a specific printer:

`lpoptions -d {{printer}} -o {{option[=value]}}`

- Remove the options of a specific printer:

`lpoptions -d {{printer}} -x`
