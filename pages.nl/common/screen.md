# screen

> Houd een sessie open op een externe server. Beheer meerdere vensters met één SSH-verbinding.
> Zie ook: `tmux` en `zellij`.
> Meer informatie: <https://manned.org/screen>.

- Start een nieuwe screen sessie:

`screen`

- Start een nieuwe benoemde screen sessie:

`screen -S {{sessie_naam}}`

- Start een nieuwe daemon en log de output van `screenlog.x`:

`screen -dmLS {{sessie_naam}} {{commando}}`

- Toon open screen sessies:

`screen -ls`

- Herkoppel aan een open screen:

`screen -r {{sessie_naam}}`

- Koppel los van binnen een screen:

`<Ctrl a><d>`

- Beëindig de huidige screen sessie:

`<Ctrl a><k>`

- Beëindig een losgekoppelde screen:

`screen -X -S {{sessie_naam}} quit`
