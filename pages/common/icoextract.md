# icoextract

> Extract icons from Windows executables (`.exe`, `.dll`, `.mun`) into ICO files.
> See also: `icolist`.
> More information: <https://github.com/jlu5/icoextract>.

- Extract the icons from an executable to an ICO file:

`icoextract {{path/to/input.exe}} {{path/to/output.ico}}`

- Extract a specific icon by its index:

`icoextract {{[-n|--num]}} {{index}} {{path/to/input.exe}} {{path/to/output.ico}}`

- Extract an icon by its resource ID:

`icoextract {{[-i|--id]}} {{resource_id}} {{path/to/input.exe}} {{path/to/output.ico}}`

- Run with verbose/debug logging:

`icoextract {{[-v|--verbose]}} {{path/to/input.exe}} {{path/to/output.ico}}`

- Display help:

`icoextract {{[-h|--help]}}`

- Display version:

`icoextract {{[-V|--version]}}`
