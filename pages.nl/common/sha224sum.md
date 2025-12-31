# sha224sum

> Bereken SHA224 cryptografische checksums.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Bereken de SHA224 checksum voor één of meer bestanden:

`sha224sum {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Bereken en sla de lijst van SHA224 checksums op in een bestand:

`sha224sum {{pad/naar/bestand1 pad/naar/bestand2 ...}} > {{pad/naar/bestand.sha224}}`

- Bereken een SHA224 checksum van `stdin`:

`{{commando}} | sha224sum`

- Lees een bestand met SHA224 checksums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`sha224sum {{[-c|--check]}} {{pad/naar/bestand.sha224}}`

- Toon alleen een bericht voor ontbrekende bestanden of wanneer verificatie mislukt:

`sha224sum {{[-c|--check]}} --quiet {{pad/naar/bestand.sha224}}`

- Toon alleen een bericht wanneer verificatie mislukt, negeer ontbrekende bestanden:

`sha224sum --ignore-missing {{[-c|--check]}} --quiet {{pad/naar/bestand.sha224}}`

- Controleer een bekende SHA224 checksum van een bestand:

`echo {{bekende_sha224_checksum_van_het_bestand}} {{pad/naar/bestand}} | sha224sum {{[-c|--check]}}`
