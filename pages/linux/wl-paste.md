# wl-paste

> Tool to access data stored in the clipboard for Wayland.
> See also: `wl-copy`.
> More information: <https://github.com/bugaevc/wl-clipboard>.

- Paste the contents of the clipboard:

`wl-paste`

- Paste the contents of the clipboard and then clear it:

`wl-paste --paste-once`

- Write the contents of the clipboard to a file:

`wl-paste > {{path/to/file}}`

- Pipe the contents of the clipboard to a command:

`wl-paste | {{command}}`

- Clear the clipboard:

`wl-paste --clear`
