# e2image

> A kritikus ext2/ext3/ext4 fájlrendszer metaadatainak mentése egy fájlba. További információ: <https://manned.org/e2image>.

- Az eszközön található metaadatok írása egy adott fájlba:

`e2image {{/dev/sdXN}} {{path/to/image_file}}`

- Az eszközön található metaadatok kiírása a `stdout` címre:

`e2image {{/dev/sdXN}} -`

- A fájlrendszer metaadatainak visszaállítása az eszközre:

`e2image -I {{/dev/sdXN}} {{path/to/image_file}}`

- Nagyméretű, nyers, ritkás fájl létrehozása a metaadatokkal a megfelelő eltolásokon:

`e2image -r {{/dev/sdXN}} {{path/to/image_file}}`

- QCOW2 képfájl létrehozása normál vagy nyers képfájl helyett:

`e2image -Q {{/dev/sdXN}} {{path/to/image_file}}`
