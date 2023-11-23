# choice

> Prompt user to select a choice and return the selected choice index.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/choice>.

- Prompt the current user to select a `Y` or `N` choice:

`choice`

- Prompt the current user to select a [c]hoice from a specific set:

`choice /c {{AB}}`

- Prompt the current user to select a choice with a specific [m]essage:

`choice /m "{{message}}"`

- Prompt the current user to select a [c]ase-[s]ensitive [c]hoice from a specific set:

`choice /cs /c {{Ab}}`

- Prompt the current user to select a choice and prefer the [d]efault choice in a specific [t]ime:

`choice /t {{5}} /d {{N}}`

- Display help:

`choice /?`
