# fsck

> A fájlrendszer integritásának ellenőrzése vagy javítása. A parancs futtatásakor a fájlrendszernek le kell lennie csatolva. A parancs egy wrapper, amely szükség szerint hívja a `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat` és `fsck_udf`. További információ: <https://ss64.com/osx/fsck.html>.

- Ellenőrizze a fájlrendszert `/dev/sdX`, jelentve a sérült blokkokat:

`fsck {{/dev/sdX}}`

- Csak akkor ellenőrzi a `/dev/sdX` fájlrendszert, ha az tiszta, minden sérült blokkot jelent, és interaktív módon lehetővé teszi a felhasználó számára, hogy az egyes blokkok javításáról döntsön:

`fsck -f {{/dev/sdX}}`

- A `/dev/sdX` fájlrendszer ellenőrzése csak akkor, ha tiszta, minden sérült blokkot jelent, és automatikusan javítja azokat:

`fsck -fy {{/dev/sdX}}`

- Ellenőrizze a `/dev/sdX` fájlrendszert, jelentve, hogy tisztán lett-e leválasztva:

`fsck -q {{/dev/sdX}}`
