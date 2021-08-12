# efibootmgr

> Manipulați Managerul de încărcare UEFI.
> Mai multe informaţii: <https://manned.org/efibootmgr>

- Listează setările curente/bootnums:

`efibootmgr`

- Listează căile de fișier:

`efibootmgr -v`

- Adăugați UEFI Shell v2 ca opțiune de boot:

`sudo efibootmgr -c -d {{/dev/sda1}} -l {{\EFI\tools\Shell.efi}} -L "{{UEFI Shell}}"`

- Modificați ordinea curentă de încărcare:

`sudo efibootmgr -o {{0002,0008,0001,0005}}`

- Ștergeți o opțiune de boot:

`sudo efibootmgr -b {{0008}} --delete-bootnum`
