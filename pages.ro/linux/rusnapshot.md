# rusnapshot

> BTRFS snapshotting utilitar scris în Rust.
> Mai multe informaţii: <https://github.com/Edu4rdSHL/rusnapshot>

- Creați un instantaneu utilizând un fișier de configurare:

`sudo rusnapshot --config {{path/to/config.toml}} --cr`

- Lista instantaneelor create:

`sudo rusnapshot -c {{path/to/config.toml}} --list`

- Ștergeți un instantaneu după ID sau numele instantaneului:

`sudo rusnapshot -c {{path/to/config.toml}} --del --id {{snapshot_id}}`

- Ștergeți toate instantaneele `oră':

`sudo rusnapshot -c {{path/to/config.toml}} --list --keep {{0}} --clean --kind {{hourly}}`

- Creați un instantaneu de citire-scriere:

`sudo rusnapshot -c {{path/to/config.toml}} --cr --rw`

- Restaurați un instantaneu:

`sudo rusnapshot -c {{path/to/config.toml}} --id {{snapshot_id}} --restore`
