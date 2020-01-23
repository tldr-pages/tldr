# efibootmgr

> Manipulate the UEFI Boot Manager (the Bootoptions).

- List the current settings:

`efibootmgr `(`-v` for Filepaths)

- Create new Bootoption:

`sudo efibootmgr -c -d {{esp_blockdevice}} -l {{\path\to\file.efi}} -L "{{Label}}"`

- > Specific Example: Adding UEFI Shell v2 as a Boot Options:

`sudo efibootmgr -c -d /dev/sda1 -l \EFI\tools\Shell.efi -L "UEFI Shell"`

- Change the current Bootorder (you can get the Bootnums from the first command):

`sudo efibootmgr -o {{0002,0008,0001,0005}}`

- Delete Bootoption:

`sudo efibootmgr -b {{bootnum}} -B`
