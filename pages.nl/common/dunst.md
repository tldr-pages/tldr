# dunst

> Een lichtgewicht en aanpasbare notificatiedaemon voor X11 en Wayland.
> Indien niet handmatig gestart, start D-Bus automatisch `dunst` op als een notificatie wordt verzonden.
> Meer informatie: <https://dunst-project.org/documentation/dunst>.

- Start `dunst`:

`dunst`

- Toon een notificatie bij het opstarten:

`dunst -startup_notification`

- Toon inkomende notificaties in `stdout`:

`dunst -print`

- Gebruik het opgegeven configuratiebestand (standaard:  `$XDG_CONFIG_HOME/dunst/dunstrc`):

`dunst {{[-conf|-config]}} {{pad/naar/bestand}}`
