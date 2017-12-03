# vim

> Vi IMproved, a programmer's text editor, providing several modes for different kinds of text manipulation.
> Pressing `i` enters edit mode. `<Esc>` goes back to normal mode, which doesn't allow regular text insertion.

- Open a file:

`vim {{file}}`

- Enter text editing mode (insert mode):

`<Esc>i`

- Copy ("yank") or cut ("delete") the current line (paste it with `P`):

`<Esc>{{yy|dd}}`

- Undo the last operation:

`<Esc>u`

- Search for a pattern in the file (press `n`/`N` to go to next/previous match):

`<Esc>/{{search_pattern}}<Enter>`

- Perform a regex substitution in the whole file:

`<Esc>:%s/{{pattern}}/{{replacement}}/g<Enter>`

- Perform a regex subtitution in the whole file using a Perl regex:

`<Esc>:perldo s/{{search_pattern}}/{{replacement}}/g<Enter>`

- Save (write) the file, and quit:

`<Esc>:wq<Enter>`

- Quit without saving:

`<Esc>:q!<Enter>`

- Write to a protected file when you forget to sudo:

`<Esc>:w !sudo tee % >/dev/null<Enter>`

- Edit a file remotely over ssh:

`vim scp://{{username}}@{{hostname}}/{{path/to/file}}`

- Open a file into existing gvim:

`gvim --remote-silent {{/path/to/file}}`
