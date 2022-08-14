# choice

> Prompt user to select a choise and return the selected choice index.
> More information: <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/choice>.

- Prompt user to select `Y` or `N` choice:

`choice`

- Prompt user to select a [c]hoice from a specific set:

`choice /c {{AB}}`

- Prompt user to select a choice with a specific [m]essage:

`choice /m "{{message}}"`

- Prompt user to select a [c]ase-[s]ensitive [c]hoice from a specific set:

`choice /cs /c {{Ab}}`

- Prompt user to select a choise and prefer the [d]efault choice in a specific [t]ime:

`choice /t {{5}} /d {{N}}`

- Display the help:

`choice /?`
