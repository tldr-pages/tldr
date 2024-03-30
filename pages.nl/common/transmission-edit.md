# transmission-edit

> Wijzig aankondigings URL's van torrentbestanden.
> Bekijk ook: `transmission`.
> Meer informatie: <https://manned.org/transmission-edit>.

- Voeg een URL toe aan of verwijder deze uit de aankondigingslijst van een torrent:

`transmission-edit --{{add|delete}} {{http://example.com}} {{pad/naar/bestand.torrent}}`

- Werk de toegangscode van een tracker bij in een torrentbestand:

`transmission-edit --replace {{oude-toegangscode}} {{nieuwe-toegangscode}} {{pad/naar/bestand.torrent}}`
