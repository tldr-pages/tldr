# sn

> Mono StrongName segédprogram IL-összeállítások aláírására és ellenőrzésére. További információ: <https://manned.org/sn>.

- Új StrongNaming kulcs generálása:

`sn -k {{path/to/key.snk}}`

- Egy összeállítás újbóli aláírása a megadott privát kulccsal:

`sn -R {{path/to/assembly.dll}} {{path/to/key_pair.snk}}`

- Az összeállítás aláírásához használt magánkulcs nyilvános kulcsának megjelenítése:

`sn -T {{path/to/assembly.exe}}`

- A nyilvános kulcs kivonása egy fájlba:

`sn -e {{path/to/assembly.dll}} {{path/to/output.pub}}`
