# psd

> Sync browser profiles between `tmpfs` and disk.
> More information: <https://manned.org/psd>.

- Show which browser profiles will be managed and their current state:

`psd {{[p|preview]}}`

- Delete all crash recovery snapshots without prompting:

`psd {{[c|clean]}}`

- Sync profiles from `tmpfs` back to disk immediately:

`psd {{sync|resync}}`

- Sync profiles back to disk, close browsers, and restore original profile directories:

`psd unsync`

- Display help:

`psd`
