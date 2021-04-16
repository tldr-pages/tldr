# efibootmgr

> Manipulate the UEFI Boot Manager (the Bootoptions).
> More information: <https://manned.org/efibootmgr>.

- List the current settings / bootnums:

`efibootmgr`

- List the filepaths:

`efibootmgr -v`

- Add UEFI Shell v2 as a boot option:

`sudo efibootmgr -c -d {{/dev/sda1}} -l {{\EFI\tools\Shell.efi}} -L "{{UEFI Shell}}"`

- Change the current boot order:

`sudo efibootmgr -o {{0002,0008,0001,0005}}`

- Delete a boot option:

`sudo efibootmgr -b {{0008}} --delete-bootnum`
