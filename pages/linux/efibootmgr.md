# efibootmgr

> Manipulate the UEFI Boot Manager.
> More information: <https://manned.org/efibootmgr>.

- List all boot options with their numbers:

`efibootmgr {{[-u|--unicode]}}`

- Add UEFI Shell v2 as a boot option:

`sudo efibootmgr {{[-c|--create]}} {{[-d|--disk]}} {{/dev/sda}} {{[-p|--part]}} {{1}} {{[-l|--loader]}} "{{path\to\shell.efi}}" {{[-L|--label]}} "{{UEFI Shell}}"`

- Add Linux as a boot option:

`sudo efibootmgr {{[-c|--create]}} {{[-d|--disk]}} {{/dev/sda}} {{[-p|--part]}} {{1}} {{[-l|--loader]}} "{{path\to\vmlinuz}}" {{[-u|--unicode]}} "{{root=UUID=12345678-90ab-cdef-1234-567890abcdef rw loglevel=3 initrd=path\to\initramfs-linux.img}}" {{[-L|--label]}} "{{Linux}}"`

- Change the current boot order:

`sudo efibootmgr {{[-o|--bootorder]}} {{0002,0008,0001,001A,...}}`

- Delete a boot option:

`sudo efibootmgr {{[-b|--bootnum]}} {{0008}} {{[-B|--delete-bootnum]}}`
