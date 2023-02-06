# asr

> Lemezkép visszaállítása (másolása) egy kötetre. A parancs neve az Apple Software Restore rövidítése. További információ: <https://www.unix.com/man-page/osx/8/asr/>.

- Lemezkép visszaállítása egy cél kötetre:

`sudo asr restore --source {{image_name}}.dmg --target {{path/to/volume}}`

- Törölje a cél kötetet a visszaállítás előtt:

`sudo asr restore --source {{image_name}}.dmg --target {{path/to/volume}} --erase`

- Visszaállítás után az ellenőrzés kihagyása:

`sudo asr restore --source {{image_name}}.dmg --target {{path/to/volume}} --noverify`

- Kötetek klónozása közbenső lemezkép használata nélkül:

`sudo asr restore --source {{path/to/volume}} --target {{path/to/cloned_volume}}`
