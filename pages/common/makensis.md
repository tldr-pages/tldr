# makensis

> Cross-platform compiler for NSIS installers.
> It compiles an NSIS script into a Windows installer executable.
> More information: <https://nsis.sourceforge.io/Docs/Chapter3.html>.

- Compile an NSIS script:

`makensis {{path/to/file.nsi}}`

- Compile an NSIS script in strict mode (treat warnings as errors):

`makensis -WX {{path/to/file.nsi}}`

- Display help for a specific command:

`makensis -CMDHELP {{command}}`
