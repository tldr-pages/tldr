# md5sum

> Bereken MD5 cryptografische checksums.
> Meer informatie: <https://www.gnu.org/software/coreutils/md5sum>.

- Bereken de MD5 checksum voor één of meer bestanden:

`md5sum {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Bereken en sla de lijst van MD5 checksums op in een bestand:

`md5sum {{pad/naar/bestand1 pad/naar/bestand2 ...}} > {{pad/naar/bestand.md5}}`

- Bereken een MD5 checksum van `stdin`:

`{{commando}} | md5sum`

- Lees een bestand met MD5 checksums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`md5sum --check {{pad/naar/bestand.md5}}`

- Toon alleen een bericht voor ontbrekende bestanden of wanneer verificatie mislukt:

`md5sum --check --quiet {{pad/naar/bestand.md5}}`

- Toon alleen een bericht wanneer verificatie mislukt, negeer ontbrekende bestanden:

`md5sum --ignore-missing --check --quiet {{pad/naar/bestand.md5}}`
