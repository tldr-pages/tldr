# birdc

> Bird remote control.
> Kommandozeilenwerkzeug zum Abrufen von Informationen wie Routen von bird und zur Durchführung von Konfigurationen während der Laufzeit.
> Weitere Informationen: <https://bird.network.cz/>.

- Öffne die remote control Konsole:

`birdc`

- Lade die Konfiguration neu, ohne Bird neu zu starten:

`birdc configure`

- Zeige den aktuellen Status von Bird an:

`birdc show status`

- Zeige alle konfigurierten Protokolle an:

`birdc show protocols`

- Zeige alle Details zu einem Protokoll an:

`birdc show protocols {{upstream1}} all`

- Zeige alle Routen an, die eine bestimmte AS-Nummer enthalten:

`birdc "show route where bgp_path ~ [{{4242120045}}]"`

- Zeige alle besten Routen an:

`birdc show route primary`

- Zeige alle Details zu allen Routen von einem bestimmten Präfix an:

`birdc show route for {{fd00:/8}} all`
