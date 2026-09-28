# partprobe

> Informeer de kernel van het besturingssysteem over wijzigingen in de partitietabel.
> Meer informatie: <https://manned.org/partprobe>.

- Informeer de kernel van het besturingssysteem over wijzigingen in de partitietabel:

`sudo partprobe`

- Informeer de kernel over wijzigingen in de partitietabel en toon een samenvatting van apparaten en hun partities:

`sudo partprobe {{[-s|--summary]}}`

- Toon een samenvatting van apparaten en hun partities zonder de kernel te informeren:

`sudo partprobe {{[-s|--summary]}} {{[-d|--dry-run]}}`
