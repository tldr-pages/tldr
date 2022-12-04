# nvim

> Neovim, a programmer's text editor based on Vim, provides several modes for different kinds of text manipulation.
> Pressing `i` in normal mode enters insert mode. `<Esc>` goes back to normal mode, which doesn't allow regular text insertion.
> See also `vim`, `vimtutor`, `vimdiff`.
> More information: <https://neovim.io>.

- Open a file:

`nvim {{path/to/file}}`

- Enter text editing mode (insert mode):

`<Esc>i`

- Copy ("yank") or cut ("delete") the current line (paste it with `P`):

`<Esc>{{yy|dd}}`

- Enter normal mode and undo the last operation:

`<Esc>u`

- Search for a pattern in the file (press `n`/`N` to go to next/previous match):

`<Esc>/{{search_pattern}}<Enter>`

- Perform a regular expression substitution in the whole file:

`<Esc>:%s/{{regular_expression}}/{{replacement}}/g<Enter>`

- Enter normal mode and save (write) the file, and quit:

`<Esc>:wq<Enter>`

- Quit without saving:

`<Esc>:q!<Enter>`
