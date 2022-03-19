# doskey

> Manage macros, windows commands and command-lines.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/doskey>.

- Print all macros:

`doskey /macros`

- Create the new macro:

`doskey {{name}} = {{command}}`

- Create the new macro for the specified executable:

`doskey /exename={{executable}} {{name}} = {{command}}`

- Remove the macro:

`doskey {{name}} =`

- Print all commands that are stored in memory:

`doskey /history`

- Save macros to the file for portability:

`doskey /macros > {{macinit}}`

- Load macros from the specified file:

`doskey /macrofile = {{macinit}}`
