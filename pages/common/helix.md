# helix

> Helix, A post-modern text editor, provides several modes for different kinds of text manipulation.
> Pressing `<i>` enters insert mode. `<Esc>` enters normal mode, which enables the use of Helix commands.
> More information: <https://manpages.debian.org/testing/hx/editor.1.en.html>.

- Open a file:

`helix {{path/to/file}}`

- Open files and show them one next each other:

`helix --vsplit {{path/to/file1 path/to/file2}}`

- Show the tutorial to learn Helix (or access it within Helix by pressing `<Esc>` and typing `<:>tutor<Enter>`):

`helix --tutor`

- Change the Helix theme:

`<:>theme {{theme_name}}`

- Save and Quit:

`<:>wq<Enter>`

- Force-quit without saving:

`<:>q!<Enter>`

- Undo the last operation:

`<u>`

- Search for a pattern in the file (press `<n>`/`<N>` to go to next/previous match):

`</>{{search_pattern}}<Enter>`
