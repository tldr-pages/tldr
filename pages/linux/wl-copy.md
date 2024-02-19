# wl-copy

> Clear and copy to Wayland clipboard.
> See also: `wl-paste`, `xclip`.
> More information: <https://github.com/bugaevc/wl-clipboard>.

- Copy the text to the clipboard:

`wl-copy "{{text}}"`

- Pipe the command (`ls`) output to the clipboard:

`{{ls}} | wl-copy`

- Copy for only one paste and then clear it:

`wl-copy --paste-once "{{text}}"`

- Copy an image:

`wl-copy < {{path/to/image}}`

- Clear the clipboard:

`wl-copy --clear`
