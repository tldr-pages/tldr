# ausearch

> Zoek in het Linux audit logboek naar gebeurtenissen.
> Onderdeel van het `audit`-pakket.
> Zie ook: `audit2why`, `audit2allow`, `aureport`.
> Meer informatie: <https://manned.org/ausearch>.

- Zoek naar alle SELinux AVC-denial gebeurtenissen:

`sudo ausearch {{[-m|--message]}} avc`

- Zoek naar gebeurtenissen die verband houden met een specifiek uitvoerbaar bestand:

`sudo ausearch {{[-c|--comm]}} {{httpd}}`

- Zoek naar gebeurtenissen van een specifieke gebruiker:

`sudo ausearch {{[-ui|--uid]}} {{1000}}`

- Zoek naar gebeurtenissen in de laatste 10 minuten:

`sudo ausearch {{[-ts|--start]}} recent`

- Zoek naar gefaalde inlogpogingen:

`sudo ausearch {{[-m|--message]}} user_login {{[-sv|--success]}} no`

- Zoek naar gebeurtenissen die verband houden met een specifiek bestand:

`sudo ausearch {{[-f|--file]}} {{pad/naar/bestand}}`

- Toon resultaten in ruwe vorm voor verdere verwerking:

`sudo ausearch {{[-m|--message]}} avc --raw`
