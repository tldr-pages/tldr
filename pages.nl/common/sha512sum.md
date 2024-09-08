# sha512sum

> Bereken SHA512 cryptografische checksums.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Bereken de SHA512 checksum voor één of meer bestanden:

`sha512sum {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Bereken en sla de lijst van SHA512 checksums op in een bestand:

`sha512sum {{pad/naar/bestand1 pad/naar/bestand2 ...}} > {{pad/naar/bestand.sha512}}`

- Bereken een SHA512 checksum van `stdin`:

`{{commando}} | sha512sum`

- Lees een bestand met SHA512 checksums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`sha512sum --check {{pad/naar/bestand.sha512}}`

- Toon alleen een bericht voor ontbrekende bestanden of wanneer verificatie mislukt:

`sha512sum --check --quiet {{pad/naar/bestand.sha512}}`

- Toon alleen een bericht wanneer verificatie mislukt, negeer ontbrekende bestanden:

`sha512sum --ignore-missing --check --quiet {{pad/naar/bestand.sha512}}`
