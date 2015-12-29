# xargs

> Execute a command with piped arguments.

- Main use:

`{{arguments}} | xargs {{command}}`

- Handle whitespace in arguments:

`{{arguments_null_terminated}} | xargs -0 {{command}}`

- Example: list unneeded packages with deborphan and remove them with apt-get:

`sudo deborphan | xargs sudo apt-get remove`

- creating variables: copy all files that start with 'M' to the Desktop

`ls M* | xargs -J % cp % ~/Desktop`
