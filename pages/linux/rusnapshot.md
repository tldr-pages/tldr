# rusnapshot

> BTRFS snapshotting utility written in Rust.
> More information: <https://github.com/Edu4rdSHL/rusnapshot>.

- Create a snapshot using a configuration file:

`sudo rusnapshot {{[-c|--config]}} {{path/to/config.toml}} --cr`

- List created snapshots:

`sudo rusnapshot {{[-c|--config]}} {{path/to/config.toml}} {{[-l|--list]}}`

- Delete a snapshot by ID or the name of the snapshot:

`sudo rusnapshot {{[-c|--config]}} {{path/to/config.toml}} --del --id {{snapshot_id}}`

- Delete all `hourly` snapshots:

`sudo rusnapshot {{[-c|--config]}} {{path/to/config.toml}} {{[-l|--list]}} {{[-k|--keep]}} {{0}} --clean --kind {{hourly}}`

- Create a read-write snapshot:

`sudo rusnapshot {{[-c|--config]}} {{path/to/config.toml}} --cr {{[-r|--rw]}}`

- Restore a snapshot:

`sudo rusnapshot {{[-c|--config]}} {{path/to/config.toml}} --id {{snapshot_id}} {{[-r|--restore]}}`
