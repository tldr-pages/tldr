# xargs

> execute a command with piped arguments

- main use

`{{arguments}} | xargs {{command}}`

- handling whitespace in arguments

`{{arguments_null_terminated}} | xargs -0 {{command}}`

- example: list unneeded packages with deborphan and remove them with apt-get

`sudo deborphan | xargs sudo apt-get remove`
