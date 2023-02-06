# diskutil

> A helyi lemezek és kötetek kezelésére szolgáló segédprogram. További információ: <https://ss64.com/osx/diskutil.html>.

- Az összes jelenleg elérhető lemez, partíció és csatlakoztatott kötet listázása:

`diskutil list`

- Egy kötet fájlrendszeri adatszerkezetének javítása:

`diskutil repairVolume {{/dev/diskX}}`

- Kötet leválasztása:

`diskutil unmountDisk {{/dev/diskX}}`

- CD/DVD lemezek kivetítése (előbb lecsatolás):

`diskutil eject {{/dev/disk1}}`
