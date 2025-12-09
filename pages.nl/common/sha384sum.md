# sha384sum

> Bereken SHA384 cryptografische checksums.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Bereken de SHA384 checksum voor één of meer bestanden:

`sha384sum {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Bereken en sla de lijst van SHA384 checksums op in een bestand:

`sha384sum {{pad/naar/bestand1 pad/naar/bestand2 ...}} > {{pad/naar/bestand.sha384}}`

- Bereken een SHA384 checksum van `stdin`:

`{{commando}} | sha384sum`

- Lees een bestand met SHA384 checksums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`sha384sum {{[-c|--check]}} {{pad/naar/bestand.sha384}}`

- Toon alleen een bericht voor ontbrekende bestanden of wanneer verificatie mislukt:

`sha384sum {{[-c|--check]}} --quiet {{pad/naar/bestand.sha384}}`

- Toon alleen een bericht wanneer verificatie mislukt, negeer ontbrekende bestanden:

`sha384sum --ignore-missing {{[-c|--check]}} --quiet {{pad/naar/bestand.sha384}}`

- Controleer een bekende SHA384 checksum van een bestand:

`echo {{bekende_sha384_checksum_van_het_bestand}} {{pad/naar/bestand}} | sha384sum {{[-c|--check]}}`
