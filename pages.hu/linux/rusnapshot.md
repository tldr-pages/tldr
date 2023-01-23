# rusnapshot

> Rust nyelven írt BTRFS snapshotoló segédprogram. További információ: <https://github.com/Edu4rdSHL/rusnapshot>.

- Pillanatkép létrehozása egy konfigurációs fájl segítségével:

`sudo rusnapshot --config {{path/to/config.toml}} --cr`

- Létrehozott pillanatfelvételek listázása:

`sudo rusnapshot -c {{path/to/config.toml}} --list`

- Pillanatkép törlése a pillanatkép azonosítója vagy neve alapján:

`sudo rusnapshot -c {{path/to/config.toml}} --del --id {{snapshot_id}}`

- Az összes `hourly` pillanatfelvétel törlése:

`sudo rusnapshot -c {{path/to/config.toml}} --list --keep {{0}} --clean --kind {{hourly}}`

- Írható-olvasható pillanatfelvétel létrehozása:

`sudo rusnapshot -c {{path/to/config.toml}} --cr --rw`

- Pillanatfelvétel visszaállítása:

`sudo rusnapshot -c {{path/to/config.toml}} --id {{snapshot_id}} --restore`
