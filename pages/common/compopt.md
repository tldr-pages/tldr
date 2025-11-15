# compopt

> Print or change the completion options for a command.
> `-o` means enabled and `+o` means disabled.
> See also: `compgen`, `complete`.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-compopt>.

- Print the completion options for given command:

`compopt {{command}}`

- Enable or disable a completion option of a command:

`compopt {{-o|+o}} {{option1}} {{-o|+o}} {{option2}} {{command}}`

- Print the options for the currently executing completion:

`compopt`

- Enable or disable a completion option of a command:

`compopt {{-o|+o}} {{option1}} {{-o|+o}} {{option2}}`
