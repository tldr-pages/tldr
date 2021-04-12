# pio system

> Miscellaneous system commands for PlatformIO.
> More information: <https://docs.platformio.org/en/latest/core/userguide/system/index.html>.

- Install shell completion for the current shell (supports bash, fish, zsh and powershell):

`pio system completion install`

- Uninstall shell completion for the current shell:

`pio system completion uninstall`

- Display system-wide PlatformIO information:

`pio system info`

- Remove unused PlatformIO data:

`pio system prune`

- Remove only cached data:

`pio system prune --cache`

- List unused PlatformIO data that would be removed but do not actually remove it:

`pio system prune --dry-run`
