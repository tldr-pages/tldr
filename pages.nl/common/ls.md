# ls

> Toon de inhoud van een map.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- Toon één bestand per regel:

`ls -1`

- Toon alle bestanden, inclusief verborgen bestanden:

`ls {{[-a|--all]}}`

- Toon alle bestanden, met een `/` achter de namen van mappen:

`ls {{[-F|--classify]}}`

- Toon alle bestanden in een [l]ange lijstweergave (permissies, eigendom, grootte en wijzigingsdatum):

`ls {{[-la|-l --all]}}`

- Toon bestanden in een [l]ange lijstweergave met grootte weergegeven in leesbare eenheden (KiB, MiB, GiB):

`ls {{[-lh|-l --human-readable]}}`

- Toon bestanden recursief in een [l]ange lijstweergave, gesorteerd op grootte (aflopend):

`ls {{[-lSR|-lS --recursive]}}`

- Toon bestanden in een [l]ange lijstweergave, gesorteerd op wijzigingsdatum (oudste eerst):

`ls {{[-ltr|-lt --reverse]}}`

- Toon alleen mappen:

`ls {{[-d|--directory]}} */`
