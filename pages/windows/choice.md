# choice

> Prompts the user to select one item from a list of single-character choices in a batch program, and then returns the index of the selected choice.
> More information: <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/choice>.

- Use the default list (`YN`) of choices:

`choice`

- Use the specified list of [c]hoices (`AB`):

`choice /c {{AB}}`

- Use the [c]ase-[s]ensitive list of choices (`AaBb`):

`choice /cs {{AaBb}}`

- Use the [d]efault choise (`A`) after a [t]imeout (`5`):

`choice /c {{AB}} /t {{5}} /d {{A}}`

- Use the specified [m]essage instead of default (`[A,B]?`):

`choice /c {{AB}} /m {{message}}`

- Print the help:

`choice /?`
