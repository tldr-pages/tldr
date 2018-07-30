# makensis

> Cross-platform compiler for NSIS installers.
> It compiles a NSIS script into a Windows installer executable.

- Compile a NSIS script:

`makensis {{path/to/file.nsi}}`

- Compile a NSIS script in strict mode (treat warnings as errors):

`makensis -WX {{path/to/file.nsi}}`

- Print help for a specific command:

`makensis -CMDHELP {{command}}`
