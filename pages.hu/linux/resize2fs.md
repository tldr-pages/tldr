# resize2fs

> Egy ext2, ext3 vagy ext4 fájlrendszer átméretezése. Az alapul szolgáló partíciót nem méretezi át. Előfordulhat, hogy a fájlrendszert először le kell csatolni, további részletekért olvassa el a man oldalt. További információ: <https://manned.org/resize2fs>.

- Automatikusan átméretez egy fájlrendszert:

`resize2fs {{/dev/sdXN}}`

- Átméretezi a fájlrendszert 40 G méretre, egy előrehaladási sávot megjelenítve:

`resize2fs -p {{/dev/sdXN}} {{40G}}`

- A fájlrendszer zsugorítása a lehető legkisebb méretre:

`resize2fs -M {{/dev/sdXN}}`
