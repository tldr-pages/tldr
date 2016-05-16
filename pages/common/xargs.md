# xargs

> Execute a command with piped arguments.

- Main use:

`{{arguments}} | xargs {{command}}`

- Specific example: delete all files that start with 'M':

`find . -name 'M*' | xargs rm`

- Handle whitespace in arguments:

`{{arguments_null_terminated}} | xargs -0 {{command}}`

- Insert arguments at chosen position, using '%' as the placeholder marker:

`{{arguments}} | xargs -I '%' {{command}} % {{extra_arguments}}`
