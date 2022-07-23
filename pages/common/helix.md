# helix

> Helix, A post-modern text editor, provides several modes for different kinds of text manipulation.
> Pressing `i` enters insert mode. `<Esc>` enters normal mode, which enables the use of Helix commands.
> More information: <https://helix-editor.com>.

- Open a file:

`helix {{path/to/file}}`

- Change the Helix theme:

`:theme {{theme_name}}`

- Save and Quit:

`:wq<Enter>`

- Force-quit without saving:

`:q!<Enter>`

- Undo the last operation:

`u`

- Search for a pattern in the file (press `n`/`N` to go to next/previous match):

`/{{search_pattern}}<Enter>`

- Format the file:

`:format`
