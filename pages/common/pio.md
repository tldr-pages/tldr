# pio

> Manage embedded development projects using PlatformIO.
> Some subcommands such as `run`, `init`, `device`, and `pkg` have their own usage documentation.
> More information: <https://docs.platformio.org/en/latest/core/userguide/>.

- Initialize a new project for a specific board:

`pio project init --board {{board_id}}`

- Build the project in the current directory:

`pio run`

- Upload firmware to the connected device:

`pio run --target upload`

- Open a serial monitor:

`pio device monitor`

- Install a library dependency:

`pio pkg install --library "{{library_name}}"`

- List all available boards:

`pio boards`

- Display help for a subcommand:

`pio {{run|init|device|pkg}} --help`
