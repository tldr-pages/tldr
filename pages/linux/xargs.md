# xargs

> Execute a command with piped arguments.

- Main use:

`{{arguments}} | xargs {{command}}`

- Handling whitespace in arguments:

`{{arguments_null_terminated}} | xargs -0 {{command}}`

- Inserting arguments at chosen position

`{{arguments}} | xargs -I piped_arguments {{command}} piped_arguments {{rest_of_arguments}}

- Example: list unneeded packages with deborphan and remove them with apt-get:

`sudo deborphan | xargs sudo apt-get remove`
