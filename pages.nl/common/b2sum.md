# b2sum

> Bereken BLAKE2 cryptografische checksums.
> Meer informatie: <https://www.gnu.org/software/coreutils/b2sum>.

- Bereken de BLAKE2 checksum voor een of meerdere bestanden:

`b2sum {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Bereken en sla de lijst van BLAKE2 checksums op in een bestand:

`b2sum {{pad/naar/bestand1 pad/naar/bestand2 ...}} > {{pad/naar/bestand.b2}}`

- Bereken de BLAKE2 checksum voor `stdin`:

`{{command}} | b2sum`

- Lees een bestand van BLAKE2 sums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`b2sum --check {{pad/naar/bestand.b2}}`

- Toon alleen een melding voor missende bestanden of als verificatie faalt:

`b2sum --check --quiet {{pad/naar/bestand.b2}}`

- Toon alleen een melding als een verificatie faalt en negeer missende bestanden:

`b2sum --ignore-missing --check --quiet {{pad/naar/bestand.b2}}`
