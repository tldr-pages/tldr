# vtool

> Display and edit Mach-O build and source version load commands.
> More information: <https://keith.github.io/xcode-man-pages/vtool.1.html>.

- Display build and source version information:

`vtool --show {{path/to/file}}`

- Display only build version information:

`vtool --show-build {{path/to/file}}`

- Display load command space information:

`vtool --show-space {{path/to/file}}`

- Display version information for a specific architecture in a universal file:

`vtool --arch {{architecture}} --show {{path/to/file}}`

- Set the source version and write the result to a new file:

`vtool --set-source-version {{A.B.C.D.E}} --output {{path/to/output_file}} {{path/to/file}}`
