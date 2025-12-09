# chroot

> Voer een commando of interactieve shell uit met een speciale hoofdmap.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- Voer `$SHELL` uit in de nieuwe hoofdmap:

`sudo chroot {{pad/naar/nieuwe/hoofdmap}}`

- Voer het commando uit als nieuwe hoofdmap:

`sudo chroot {{pad/naar/nieuwe/hoofdmap}} {{commando}}`

- Gebruik een specifieke gebruiker en groep:

`sudo chroot --userspec {{gebruikersnaam_of_id}}:{{groep_naam_of_id}} {{pad/naar/nieuwe/hoofdmap}}`
