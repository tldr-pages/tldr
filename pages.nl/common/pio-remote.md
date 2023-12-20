# pio remote

> Helper commando voor PlatformIO Remote Development.
> `pio remote [commando]` accepteert dezelfde argumenten als de lokale tegenhanger `pio [commando]`.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/remote/index.html>.

- Toon alle actieve Remote Agents:

`pio remote agent list`

- Start een nieuwe Remote Agent met een specifieke naam en deel deze met vrienden:

`pio remote agent start --name {{agent_naam}} --share {{example1@example.com}} --share {{example2@example.com}}`

- Toon alle apparaten van een specifieke Agents (laat `--agent` weg voor alle Agents):

`pio remote --agent {{agent_naam1}} --agent {{agent_naam2}} device list`

- Verbind met een seriele poort van een remote apparaat:

`pio remote --agent {{agent_naam}} device monitor`

- Voer alle doelen uit op een gespecificeerde Agent:

`pio remote --agent {{agent_naam}} run`

- Update geïnstalleerde kern pakketten, ontwikkelplatformen en globale bibliotheken op een specifieke Agent:

`pio remote --agent {{agent_naam}} update`

- Voer alle testen uit in alle omgevingen op een specifieke Agent:

`pio remote --agent {{agent_naam}} test`
