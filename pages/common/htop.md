# htop

> Display dynamic real-time information about running processes.
> An enhanced version of `top`.
> See also: `top`, `atop`, `glances`, `btop`, `btm`.
> More information: <https://manned.org/htop>.

- Start `htop`:

`htop`

- Start `htop` displaying processes owned by a specific user:

`htop {{[-u|--user]}} {{username}}`

- Display processes hierarchically in a tree view to show the parent-child relationships:

`htop {{[-t|--tree]}}`

- Sort processes by a specified `sort_item` (use `htop --sort help` for available options):

`htop {{[-s|--sort]}} {{sort_item}}`

- Start `htop` with the specified delay between updates, in tenths of a second (i.e. 50 = 5 seconds):

`htop {{[-d|--delay]}} {{50}}`

- Disable all system and process changing features:

`htop --readonly`

- See interactive commands while running `htop`:

`{{<F1>|<?>}}`

- Switch to a different tab:

`<Tab>`
