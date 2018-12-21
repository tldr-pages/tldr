# gibo

> Fetch gitignore boilerplates.

- List available boilerplates:

`gibo list`

- Write a boilerplate to stdout:

`gibo dump {{boilerplate}}`

- Write a boilerplate to .gitignore:

`gibo dump {{boilerplate}} >>{{.gitignore}}`

- Search for boilerplates containing a given string:

`gibo search {{string}}`

- Update available local boilerplates:

`gibo update`
