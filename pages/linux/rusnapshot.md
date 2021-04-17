# rusnapshot

> BTRFS snapshotting utility made in Rust.
> More information: <https://github.com/Edu4rdSHL/rusnapshot>.

- Create a snapshot using a config file:

`sudo rusnapshot --config {{/path/to/config.toml}} --cr`

- List created snapshots:

`sudo rusnapshot -c {{/path/to/config.toml}} -l`

- Delete a snapshot by ID or the name of the snapshot:

`sudo rusnapshot -c {{/path/to/config.toml}} --del --id {{snapshot_id}}`

- Delete all snapshots of [kind] three-hours:

`sudo rusnapshot -c {{/path/to/config.toml}}  -l -k 0 --clean --kind three-hours`
