# dd

> Converteer en kopieer een bestand.
> Meer informatie: <https://manned.org/man/dd.1p>.

- Maak een opstartbare USB-schijf van een isohybrid-bestand (zoals `archlinux-xxx.iso`):

`dd if={{pad/naar/bestand.iso}} of=/dev/{{usb_schijf}}`

- Kopieer een schijf naar een andere schijf met een blokgrootte van 4 MiB en schrijf alle gegevens voordat het commando eindigt:

`dd bs=4194304 conv=fsync if=/dev/{{bron_schijf}} of=/dev/{{doel_schijf}}`

- Genereer een bestand met een specifiek aantal willekeurige bytes met behulp van de kernel random driver:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{pad/naar/willekeurig_bestand}}`

- Benchmark de sequentiële schrijfsnelheid van een schijf:

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{pad/naar/bestand_1GB}}`

- Maak een systeemback-up en sla deze op in een IMG bestand (kan later worden hersteld door `if` en `of` om te wisselen):

`dd if={{/dev/schijf_apparaat}} of={{pad/naar/bestand.img}}`
