# encfs

> Titkosított virtuális fájlrendszerek csatolása vagy létrehozása. Lásd még: `fusermount`, amely az ezzel a paranccsal csatolt fájlrendszerek csatolásának megszüntetésére szolgál. További információ: <https://github.com/vgough/encfs>.

- Titkosított fájlrendszer inicializálása vagy csatolása:

`encfs {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- Titkosított fájlrendszer inicializálása szabványos beállításokkal:

`encfs --standard {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- Az encfs futtatása előtérben a démon indítása helyett:

`encfs -f {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- Egy sima könyvtár titkosított pillanatfelvételének csatolása:

`encfs --reverse {{path/to/plain_dir}} {{path/to/cipher_dir}}`
