# timeshift

> System restore utility.
> More information: <https://github.com/teejee2008/timeshift>.

- List snapshots:

`sudo timeshift --list`

- Create a new snapshot (if scheduled):

`sudo timeshift --check`

- Create a new snapshot (even if not scheduled):

`sudo timeshift --create`

- Restore a snapshot (selecting which snapshot to restore interactively):

`sudo timeshift --restore`

- Restore a specific snapshot:

`sudo timeshift --restore --snapshot '{{snapshot}}'`

- Delete a specific snapshot:

`sudo timeshift --delete --snapshot '{{snapshot}}'`
