# goku

> Manage Karabiner configuration.
> More information: <https://github.com/yqrashawn/GokuRakuJoudo>.

- Generate `karabiner.json` using the default configuration:

`goku`

- Generate `karabiner.json` using the specific `config.edn` file:

`goku --config {{path/to/config.edn}}`

- Dry run the new configuration into `stdout` instead of updating `karabiner.json`:

`goku --dry-run`

- Dry run the whole configuration into `stdout` instead of updating `karabiner.json`:

`goku --dry-run-all`

- Display help:

`goku --help`

- Display version:

`goku --version`
