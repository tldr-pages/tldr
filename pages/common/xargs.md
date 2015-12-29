# xargs

> Execute a command with piped arguments.

- Main use:

`{{arguments}} | xargs {{command}}`

- Handle whitespace in arguments:

`{{arguments_null_terminated}} | xargs -0 {{command}}`

- delete all files that start with 'M'

`ls M* | xargs rm`

- assign incoming arguments to a variable so that they may be used in the middle of a command

`ls M* | xargs -J % cp % ~/Desktop`
