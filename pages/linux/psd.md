# psd

> Profile-sync-daemon: keep browser profiles in `tmpfs` and sync them back to disk periodically.
> It normally runs as a systemd user service called `psd`.
> More information: <https://manned.org/psd>.

- Show which browser profiles will be managed and their current state:

`psd {{[p|preview]}}`

- Delete all crash recovery snapshots without prompting:

`psd {{[c|clean]}}`

- Sync profiles from `tmpfs` back to disk immediately:

`psd sync`

- Resync profiles from `tmpfs` back to disk (same as `sync`, normally run hourly by `psd-resync.timer`):

`psd resync`

- Sync profiles back to disk, close running browsers, and restore the original profile directories:

`psd unsync`

- Display help:

`psd`
