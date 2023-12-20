# pio system

> Gemengde systeem commando's voor PlatformIO.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/system/>.

- Installeer shell completion voor de huidige shell (ondersteund Bash, Fish, Zsh en PowerShell):

`pio system completion install`

- Deinstalleer shell completion voor de huidige shell:

`pio system completion uninstall`

- Toon systeem-wijde PlatformIO informatie:

`pio system info`

- Verwijder ongebruikte PlatformIO data:

`pio system prune`

- Verwijder alleen gecachte data:

`pio system prune --cache`

- Toon ongebruikte PlatformIO data die verwijderd zou worden, maar verwijder het niet echt:

`pio system prune --dry-run`
