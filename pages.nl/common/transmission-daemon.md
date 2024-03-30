# transmission-daemon

> Daemon bediend met `transmission-remote` of de webinterface.
> Bekijk ook: `transmission`.
> Meer informatie: <https://manned.org/transmission-daemon>.

- Start een headless `transmission` sessie:

`transmission-daemon`

- Start en bewaak een specifieke map voor nieuwe torrents:

`transmission-daemon --watch-dir {{pad/naar/map}}`

- Dump daemon-instellingen in JSON formaat:

`transmission-daemon --dump-settings > {{pad/naar/bestand.json}}`

- Start met specifieke instellingen voor de web interface:

`transmission-daemon --auth --username {{gebruikersnaam}} --password {{wachtwoord}} --port {{9091}} --allowed {{127.0.0.1}}`
