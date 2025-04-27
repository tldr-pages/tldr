# pio run

> Run PlatformIO project targets.
> More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_run.html>.

- List all available project targets:

`pio run --list-targets`

- List all available project targets of a specific environment:

`pio run --list-targets {{[-e|--environment]}} {{environment}}`

- Run all targets:

`pio run`

- Run all targets of specified environments:

`pio run {{[-e|--environment]}} {{environment1}} {{[-e|--environment]}} {{environment2}}`

- Run specified targets:

`pio run {{[-t|--target]}} {{target1}} {{[-t|--target]}} {{target2}}`

- Run the targets of a specified configuration file:

`pio run {{[-c|--project-conf]}} {{path/to/platformio.ini}}`
