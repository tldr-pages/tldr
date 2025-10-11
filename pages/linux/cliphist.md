# cliphist

> Manage clipboard history for Wayland compositors.
> Works with `wl-copy` and `wl-paste`.
> More information: <https://github.com/sentriz/cliphist>.

- List clipboard history entries:

`cliphist list`

- Select and copy a previous clipboard entry (using `fzf`):

`cliphist list | fzf | cliphist decode | wl-copy`

- Delete all stored clipboard entries:

`cliphist wipe`

- Delete a specific clipboard entry by ID:

`cliphist delete {{id}}`

- Save the current clipboard content manually:

`wl-paste | cliphist store`
