# lpoptions

> Display or set printer options and defaults.
> See also: `lpadmin`.
> More information: <https://openprinting.github.io/cups/doc/man-lpoptions.html>.

- Set the default printer:

`lpoptions -d {{printer}}/{{instance}}`

- List printer options for the default printer:

`lpoptions -l`

- List currently set options of a specific printer:

`loptions -p {{printer}}`

- List what options the driver exposes for a printer:

`lpoptions -p {{printer}} -l`

- Set a new option on the default printer:

`lpoptions -o {{option}}`

- Remove the options of a specific printer:

`lpoptions -x {{printer}}`
