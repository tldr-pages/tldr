# sha1sum

> Bereken SHA1 cryptografische checksums.
> Meer informatie: <https://www.gnu.org/software/coreutils/sha1sum>.

- Bereken de SHA1 checksum voor één of meer bestanden:

`sha1sum {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Bereken en sla de lijst van SHA1 checksums op in een bestand:

`sha1sum {{pad/naar/bestand1 pad/naar/bestand2 ...}} > {{pad/naar/bestand.sha1}}`

- Bereken een SHA1 checksum van `stdin`:

`{{commando}} | sha1sum`

- Lees een bestand met SHA1 checksums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`sha1sum --check {{pad/naar/bestand.sha1}}`

- Toon alleen een bericht voor ontbrekende bestanden of wanneer verificatie mislukt:

`sha1sum --check --quiet {{pad/naar/bestand.sha1}}`

- Toon alleen een bericht wanneer verificatie mislukt, negeer ontbrekende bestanden:

`sha1sum --ignore-missing --check --quiet {{pad/naar/bestand.sha1}}`
