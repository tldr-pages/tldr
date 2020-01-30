# efibootmgr

> Manipulate the UEFI Boot Manager (the Bootoptions).

- List the current settings:

`efibootmgr -v for Filepaths`

- Create a new boot option:

`sudo efibootmgr -c -d {{esp_blockdevice}} -l {{\path\to\file.efi}} -L "{{Label}}"`

- Add UEFI Shell v2 as a boot option:

`sudo efibootmgr -c -d /dev/sda1 -l \EFI\tools\Shell.efi -L "UEFI Shell"`

- Change the current boot order (you can get the Bootnums from the first command):

`sudo efibootmgr -o {{0002,0008,0001,0005}}`

- Delete a boot option:

`sudo efibootmgr -b {{bootnum}} -B`
