# rusnapshot

> BTRFS snapshotting utility written in Rust.
> More information: <https://github.com/Edu4rdSHL/rusnapshot>.

- Create a snapshot using a config file:

`sudo rusnapshot --config {{/path/to/config.toml}} --cr`

- List created snapshots:

`sudo rusnapshot --config {{/path/to/config.toml}} --list`

- Delete a snapshot by ID or the name of the snapshot:

`sudo rusnapshot --config {{/path/to/config.toml}} --del --id {{snapshot_id}}`

- Delete all snapshots of [kind] three-hours:

`sudo rusnapshot --config {{/path/to/config.toml}}  --list --keep 0 --clean --kind {{three-hours}}`
