# xargs

> execute a command with piped arguments

- main use

`{{arguments}} | xargs {{command}}`

- handling whitespace in arguments

`{{arguments_null_terminated}} | xargs -0 {{command}}`

- find all zip files and extract with unzip function

`find . -type f -name "*.zip" | xargs unzip`

- find all text files containing the string 'foo'

`find . -name '*.txt' | xargs grep 'foo'`
