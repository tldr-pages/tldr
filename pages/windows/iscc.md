# iscc

> Compiler for Inno Setup installers.
> It compiles an Inno Setup scripts into an Windows installer executable.

- Compile an Inno Setup script:

`iscc {{path/to/file.iss}}`

- Quietly compile an Inno Setup installer:

`iscc /Q {{path/to/file.iss}}`

- Compile a signed Inno Setup installer:

`iscc /S={{name}}={{command}} {{path/to/file.iss}}`
