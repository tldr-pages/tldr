# sync

> Schrijft alle hangende schrijfoperaties naar de juiste schijven.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/sync-invocation.html>.

- Schrijf alle hangende schrijfoperaties naar alle schijven:

`sync`

- Schrijf alle hangende schrijfoperaties van een enkel bestand naar de schijf:

`sync {{pad/naar/bestand}}`

- Schrijf alle schrijfoperaties en verwijder caches van het bestandssysteem (alleen voor Linux):

`sync; echo 3 | sudo tee /proc/sys/vm/drop_caches`

- Voer schijf schrijfoperaties uit en probeer inactief geheugen en caches van het bestandssysteem te wissen (alleen voor MacOS):

`sync; sudo purge`
