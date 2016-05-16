# xargs

> Execute a command with piped arguments.

- Main use:

`{{arguments}} | xargs {{command}}`

- Handle whitespace in arguments:

`{{arguments_null_terminated}} | xargs -0 {{command}}`

- Insert arguments at chosen position, using '%' as the placeholder marker:

`{{arguments}} | xargs -I '%' {{command}} % {{extra_arguments}}`

- Use the output of one command as arguments to another command:

`{{command1}} | xargs {{command2}}`

- Specific example: delete all files that start with 'M':

`find . -name 'M*' | xargs rm`
