# sync

> Schrijft alle hangende schrijfoperaties naar de juiste schijven.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/sync-invocation.html>.

- Schrijf alle hangende schrijfoperaties naar alle schijven:

`sync`

- Schrijf alle hangende schrijfoperaties van een enkel bestand naar de schijf:

`sync {{pad/naar/bestand}}`

- Schrijf alle schrijfoperaties en verwijder caches van het bestandssysteem:

`sync; echo 3 | sudo tee /proc/sys/vm/drop_caches`
