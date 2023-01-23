# efibootmgr

> Az UEFI Boot Manager kezelése. További információ: <https://manned.org/efibootmgr>.

- Az aktuális beállítások listázása, majd bootnums a nevükkel:

`efibootmgr`

- Listázza a fájlútvonalakat:

`efibootmgr -v`

- Hozzáadja az UEFI Shell v2-t mint bootolási opciót:

`sudo efibootmgr -c -d {{/dev/sda1}} -l {{\EFI\tools\Shell.efi}} -L "{{UEFI Shell}}"`

- Az aktuális indítási sorrend megváltoztatása:

`sudo efibootmgr -o {{0002,0008,0001,0005}}`

- Bootolási opció törlése:

`sudo efibootmgr -b {{0008}} --delete-bootnum`
