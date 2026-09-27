# parted

> Een programma voor het manipuleren van partities.
> Zie ook: `parted.interactive`, `cfdisk`, `partprobe`.
> Meer informatie: <https://www.gnu.org/software/parted/manual/parted.html#Invoking-Parted>.

- Toon partities op alle blokapparaten:

`sudo parted {{[-l|--list]}}`

- Maak een nieuwe partitietabel van het gespecificeerde label-type:

`sudo parted {{/dev/sdX}} mklabel {{aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun}}`

- Maak een nieuwe `gpt`-partitietabel met een boot-partitie van 500MiB en geef de rest aan de systeempartitie (`--script` slaat gebruikersinvoerverzoeken over):

`sudo parted {{/dev/sdX}} {{[-s|--script]}} mklabel gpt mkpart "{{boot_partitie_naam}}" 0% 500MiB mkpart "{{systeem_partitie_naam}}" 500MiB 100%`

- Stel een partitie in met de boot-vlag ingeschakeld:

`sudo parted {{/dev/sdX}} set {{1}} boot on`

- Start interactieve modus met de gespecificeerde schijf geselecteerd:

`sudo parted {{/dev/sdX}}`

- Toon de help:

`parted {{[-h|--help]}}`
