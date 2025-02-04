# dtrx

> "Do The Right eXtraction" - don't remember what set of tar flags or where to pipe the output to extract it? no worries!
> More information: <https://github.com/dtrx-py/dtrx>.

- Extract archive, guessing the tool from extension:

`dtrx {{foo}}`

- Extract archive, overwrite any existing target output:

`dtrx --overwrite {{foo}}`

- Extract archive, extract everything into current directory:

`dtrx --flat {{foo}}`
