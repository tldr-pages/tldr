# gio

> Beheer lokale en virtuele bestanden (GVfs).
> Onderdeel van GLib dat gebruikt wordt in GNOME-gebaseerde systemen.
> Meer informatie: <https://manned.org/gio>.

- Open een bestand met de standaardapplicatie (bijv. PDF, afbeelding):

`gio open {{pad/naar/bestand}}`

- Toon bestanden in een map:

`gio list {{pad/naar/map}}`

- Toon informatie over een bestand:

`gio info {{pad/naar/bestand}}`

- Kopieer een bestand:

`gio copy {{pad/naar/bron}} {{pad/naar/bestemming}}`

- Stuur een bestand naar de prullenbak (omkeerbaar):

`gio trash {{pad/naar/bestand}}`

- Leeg de prullenbak:

`gio trash --empty`

- Start een applicatie vanuit een `.desktop` bestand:

`gio launch {{pad/naar/bestand}}.desktop`

- Markeer een `.desktop` bestand als vertrouwd, waardoor het uitgevoerd kan worden:

`gio set {{pad/naar/bestand}}.desktop metadata::trusted true`
