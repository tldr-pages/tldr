# ls

> Toon de inhoud van een map.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- Toon één bestand per regel:

`ls -1`

- Toon alle bestanden, inclusief verborgen bestanden:

`ls {{[-a|--all]}}`

- Toon alle bestanden, met een `/` achter de namen van mappen:

`ls {{[-F|--classify]}}`

- Lange lijstweergave (permissies, eigendom, grootte en wijzigingsdatum) van alle bestanden:

`ls {{[-la|--all -l]}}`

- Lange lijstweergave met grootte weergegeven in leesbare eenheden (KiB, MiB, GiB):

`ls {{[-lh|-l --human-readable]}}`

- Lange lijstweergave gesorteerd op grootte (aflopend) recursief:

`ls {{[-lSR|-lS --recursive]}}`

- Lange lijstweergave van alle bestanden, gesorteerd op wijzigingsdatum (oudste eerst):

`ls {{[-ltr|-lt --reverse]}}`

- Toon alleen mappen:

`ls {{[-d|--directory]}} */`
