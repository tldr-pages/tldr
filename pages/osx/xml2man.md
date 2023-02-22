# xml2man

> Compile MPGL to mdoc.
> More information: <https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/mpgl/mpgl.html>.

- Compile an MPGL file to a viewable man page:

`xml2man {{path/to/command_file.mxml}}`

- Compile an MPGL file to a specific output file:

`xml2man {{path/to/service_file.mxml}} {{path/to/service_file.7}}`

- Compile an MPGL file to a specific output file, overwriting if it already exists:

`xml2man -f {{path/to/function_file.mxml}} {{path/to/function_file.3}}`
