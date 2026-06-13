# sha256sum

> Bereken SHA256 cryptografische checksums.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Bereken de SHA256 checksum voor één of meer bestanden:

`sha256sum {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Bereken en sla de lijst van SHA256 checksums op in een bestand:

`sha256sum {{pad/naar/bestand1 pad/naar/bestand2 ...}} > {{pad/naar/bestand.sha256}}`

- Bereken een SHA256 checksum van `stdin`:

`{{commando}} | sha256sum`

- Lees een bestand met SHA256 checksums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`sha256sum {{[-c|--check]}} {{pad/naar/bestand.sha256}}`

- Toon alleen een bericht voor ontbrekende bestanden of wanneer verificatie mislukt:

`sha256sum {{[-c|--check]}} --quiet {{pad/naar/bestand.sha256}}`

- Toon alleen een bericht wanneer verificatie mislukt, negeer ontbrekende bestanden:

`sha256sum --ignore-missing {{[-c|--check]}} --quiet {{pad/naar/bestand.sha256}}`

- Controleer een bekende SHA256 checksum van een bestand:

`echo {{bekende_sha256_checksum_van_een_bestand}} {{pad/naar/bestand}} | sha256sum {{[-c|--check]}}`
