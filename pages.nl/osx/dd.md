# dd

> Converteer en kopieer een bestand.
> Meer informatie: <https://keith.github.io/xcode-man-pages/dd.1.html>.

- Maak een opstartbare USB-schijf van een isohybrid-bestand (zoals `archlinux-xxx.iso`) en toon de voortgang:

`dd if={{pad/naar/bestand.iso}} of={{/dev/usb_apparaat}} status=progress`

- Kopieer een schijf naar een andere schijf met een blokgrootte van 4 MiB, negeer fouten en toon de voortgang:

`dd bs=4m conv=noerror if={{/dev/bron_apparaat}} of={{/dev/doel_apparaat}} status=progress`

- Genereer een bestand met een specifiek aantal willekeurige bytes met behulp van de kernel random driver:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{path/to/random_file}}`

- Benchmark de schrijfsnelheid van een schijf:

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{pad/naar/bestand_1GB}}`

- Maak een systeemback-up, sla deze op in een IMG bestand (kan later worden hersteld door `if` en `of` om te wisselen) en toon de voortgang:

`dd if={{/dev/schijf_apparaat}} of={{pad/naar/bestand.img}} status=progress`

- Bekijk de voortgang van een lopende `dd` operatie (voer dit commando uit vanaf een andere shell)::

`kill -USR1 $(pgrep ^dd)`
