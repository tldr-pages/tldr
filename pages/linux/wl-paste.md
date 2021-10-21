# wl-paste

> Tool to access data stored in the clipboard for Wayland.
> Pairs well with wl-copy.
> More information: <https://manned.org/wl-paste>.

- Output the contents of the clipboard:

`wl-paste`

- Paste the contents of the clipboard once then clear the clipboard:

`wl-paste --paste-once`

- Paste the contents of the clipboard to a file:

`wl-paste > {{filename}}`

- Pipe the contents of the clipboard to a command:

`wl-paste | {{command}}`

- Clear the clipboard:

`wl-paste --clear`
