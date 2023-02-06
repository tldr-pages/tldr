# pio run

> PlatformIO projektcélok futtatása. További információ: <https://docs.platformio.org/en/latest/core/userguide/cmd_run.html>.

- Az összes elérhető projektcélpont listája:

`pio run --list-targets`

- Egy adott környezet összes elérhető projektcéljának listázása:

`pio run --list-targets --environment {{environment}}`

- Az összes célpont futtatása:

`pio run`

- A megadott környezetek összes célpontjának futtatása:

`pio run --environment {{environment1}} --environment {{environment2}}`

- Meghatározott célok futtatása:

`pio run --target {{target1}} --target {{target2}}`

- Egy megadott konfigurációs fájl célpontjainak futtatása:

`pio run --project-conf {{path/to/platformio.ini}}`
