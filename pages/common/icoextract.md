# icoextract

> Extract icons from Windows executables (.exe, .dll, .mun) into .ico files.
> More information: <https://github.com/jlu5/icoextract>.

- Extract the icon(s) from an executable to an ICO file:

`icoextract {{path/to/input.exe}} {{path/to/output.ico}}`

- Extract a specific icon by its index:

`icoextract --num {{index}} {{path/to/input.exe}} {{path/to/output.ico}}`

- Extract an icon by its resource ID:

`icoextract --id {{resource_id}} {{path/to/input.exe}} {{path/to/output.ico}}`

- Run with verbose/debug logging:

`icoextract --verbose {{path/to/input.exe}} {{path/to/output.ico}}`

- Display the installed version:

`icoextract --version`