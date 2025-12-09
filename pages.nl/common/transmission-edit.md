# transmission-edit

> Wijzig aankondigings URL's van torrentbestanden.
> Zie ook: `transmission`.
> Meer informatie: <https://manned.org/transmission-edit>.

- Voeg een URL toe aan de aankondigingslijst van een torrent:

`transmission-edit {{[-a|--add]}} {{http://example.com}} {{pad/naar/bestand.torrent}}`

- Verwijder een URL van de aankondigingslijst van een torrent:

`transmission-edit {{[-d|--delete]}} {{http://example.com}} {{pad/naar/bestand.torrent}}`

- Werk de toegangscode van een tracker bij in een torrentbestand:

`transmission-edit {{[-r|--replace]}} {{oude-toegangscode}} {{nieuwe-toegangscode}} {{pad/naar/bestand.torrent}}`
