# b2sum

> Bereken BLAKE2 cryptografische checksums.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/b2sum-invocation.html>.

- Bereken de BLAKE2 checksum voor een of meerdere bestanden:

`b2sum {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Bereken en sla de lijst van BLAKE2 checksums op in een bestand:

`b2sum {{pad/naar/bestand1 pad/naar/bestand2 ...}} > {{pad/naar/bestand.b2}}`

- Bereken de BLAKE2 checksum voor `stdin`:

`{{commando}} | b2sum`

- Lees een bestand van BLAKE2 sums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`b2sum {{[-c|--check]}} {{pad/naar/bestand.b2}}`

- Toon alleen een melding voor missende bestanden of als verificatie faalt:

`b2sum {{[-c|--check]}} --quiet {{pad/naar/bestand.b2}}`

- Toon alleen een melding als een verificatie faalt en negeer missende bestanden:

`b2sum --ignore-missing {{[-c|--check]}} --quiet {{pad/naar/bestand.b2}}`

- Controleer een bekende BLAKE2 checksum van een bestand:

`echo {{bekende_blake2_checksum_van_het_bestand}} {{pad/naar/bestand}} | b2sum {{[-c|--check]}}`
