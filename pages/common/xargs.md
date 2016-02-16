# xargs

> Execute a command with piped arguments.

- Main use:

`{{arguments}} | xargs {{command}}`

- Handle whitespace in arguments:

`{{arguments_null_terminated}} | xargs -0 {{command}}`

- Delete all files that start with 'M':

`find . -name 'M*' | xargs rm`

- Inserting arguments at chosen position:

`{{arguments}} | xargs -I piped_arguments {{command}} piped_arguments {{rest_of_arguments}}
