# more

> Display paginated output from `stdin` or a file.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/more>.

- Display paginated output from `stdin`:

`{{echo test}} | more`

- Display paginated output from one or more files:

`more {{path\to\file}}`

- Convert tabs to the specified number of spaces:

`more {{path\to\file}} /t{{spaces}}`

- Clear the screen before displaying the page:

`more {{path\to\file}} /c`

- Display the output starting at line 5:

`more {{path\to\file}} +{{5}}`

- Enable extended interactive mode (see help for usage):

`more {{path\to\file}} /e`

- Display full usage information:

`more /?`
