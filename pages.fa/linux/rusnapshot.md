# rusnapshot

> ابزار snapshotگیری BTRFS نوشته‌شده با Rust.
> اطلاعات بیشتر: <https://github.com/Edu4rdSHL/rusnapshot>.

- ایجاد snapshot با فایل پیکربندی:

`sudo rusnapshot {{[-c|--config]}} {{path/to/config.toml}} --cr`

- فهرست کردن snapshotهای ایجادشده:

`sudo rusnapshot {{[-c|--config]}} {{path/to/config.toml}} {{[-l|--list]}}`

- حذف snapshot با شناسه یا نام آن:

`sudo rusnapshot {{[-c|--config]}} {{path/to/config.toml}} --del --id {{snapshot_id}}`

- حذف همهٔ snapshotهای `hourly`:

`sudo rusnapshot {{[-c|--config]}} {{path/to/config.toml}} {{[-l|--list]}} {{[-k|--keep]}} {{0}} --clean --kind {{hourly}}`

- ایجاد snapshot خواندنی و نوشتنی:

`sudo rusnapshot {{[-c|--config]}} {{path/to/config.toml}} --cr {{[-r|--rw]}}`

- بازیابی snapshot:

`sudo rusnapshot {{[-c|--config]}} {{path/to/config.toml}} --id {{snapshot_id}} {{[-r|--restore]}}`
