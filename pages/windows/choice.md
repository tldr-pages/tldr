# choice

> Prompts the user to select one item from a list of single-character choices in a batch program, and then returns the index of the selected choice.
> If used without parameters, choice displays the default choices Y and N.
> More information: <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/choice>.

- A,B and C as list of choices to be used:

`choice /c {{ABC}}`

- Use the default [Y,N] list of choices:

`choice`

- Specify that the choices are case-sensitive:

`choice /CS {{AaBb}}`

- Specify the number of seconds to pause before using the default choice specified by `/d`:

`choice /C {{AaBb}} /t {{3}} /d {{b}}`

- Specify a message to display before the list of choices. If `/m` is not specified, only the choice prompt is displayed:

`choice /m {{message}} /C {{ABC}}`

- Display help message:

`choice /?`
