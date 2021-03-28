# pio system

> Miscellaneous system commands for PlatformIO.
> More information: <https://docs.platformio.org/en/latest/core/userguide/system/index.html>.

- Install shell completion for the current shell (supports fish, bash, zsh and powershell):

`pio system completion install`

- Uninstall shell completion for the current shell:

`pio system completion uninstall`

- Print system-wide PlatformIO information:

`pio system info`

- Remove unused PlatformIO data:

`pio system prune`

- Remove only cached data:

`pio system prune --cache`

- Show unused PlatformIO data to be removed without removing it:

`pio system prune --dry-run`
