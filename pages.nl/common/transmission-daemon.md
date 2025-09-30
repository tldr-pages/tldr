# transmission-daemon

> Daemon bediend met `transmission-remote` of de webinterface.
> Zie ook: `transmission`.
> Meer informatie: <https://manned.org/transmission-daemon>.

- Start een headless `transmission` sessie:

`transmission-daemon`

- Start en bewaak een specifieke map voor nieuwe torrents:

`transmission-daemon {{[-c|--watch-dir]}} {{pad/naar/map}}`

- Dump daemon-instellingen in JSON formaat:

`transmission-daemon {{[-d|--dump-settings]}} > {{pad/naar/bestand.json}}`

- Start met specifieke instellingen voor de web interface:

`transmission-daemon {{[-t|--auth]}} {{[-u|--username]}} {{gebruikersnaam}} {{[-v|--password]}} {{wachtwoord}} {{[-p|--port]}} {{9091}} {{[-a|--allowed]}} {{127.0.0.1}}`
