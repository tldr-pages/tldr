# fsck

> A fájlrendszer integritásának ellenőrzése vagy javítása. A parancs futtatásakor a fájlrendszernek le kell lennie csatolva. További információ: <https://manned.org/fsck>.

- A fájlrendszer ellenőrzése `/dev/sdXN`, a sérült blokkok jelentése:

`sudo fsck {{/dev/sdXN}}`

- Check filesystem `/dev/sdXN`, amely minden sérült blokkot jelent, és interaktív módon lehetővé teszi a felhasználó számára, hogy az egyes blokkok javítását kiválassza:

`sudo fsck -r {{/dev/sdXN}}`

- A fájlrendszer ellenőrzése `/dev/sdXN`, amely minden sérült blokkot jelent, és automatikusan javítja azokat:

`sudo fsck -a {{/dev/sdXN}}`
