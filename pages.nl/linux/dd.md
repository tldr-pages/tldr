# dd

> Converteer en kopieer een bestand.
> Zie ook: `caligula`.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html>.

- Maak een opstartbare USB-schijf van een isohybrid-bestand (zoals `archlinux-xxx.iso`) en toon de voortgang:

`sudo dd if={{pad/naar/bestand.iso}} of={{/dev/usb_schijf}} status=progress`

- Kopieer een schijf naar een andere schijf met een blokgrootte van 4 MiB en schrijf alle gegevens voordat het commando eindigt:

`sudo dd bs=4M conv=fsync if={{/dev/bron_schijf}} of={{/dev/doel_schijf}}`

- Genereer een bestand met een specifiek aantal willekeurige bytes met behulp van de kernel random driver:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{pad/naar/willekeurig_bestand}}`

- Benchmark de sequentiële schrijfsnelheid van een schijf:

`dd bs={{1M}} count={{1024}} if=/dev/zero of={{pad/naar/bestand_1GB}}`

- Maak een systeemback-up, sla deze op in een IMG bestand (kan later worden hersteld door `if` en `of` om te wisselen) en toon de voortgang:

`dd if={{/dev/schijf_apparaat}} of={{pad/naar/bestand.img}} status=progress`

- Bekijk de voortgang van een lopende `dd` operatie (voer dit commando uit vanaf een andere shell):

`progress`
