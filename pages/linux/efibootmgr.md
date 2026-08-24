# efibootmgr

> Manipulate the UEFI Boot Manager.
> More information: <https://manned.org/efibootmgr>.

- List all boot options with their numbers:

`efibootmgr {{[-u|--unicode]}}`

- Add a UEFI executable (e.g. UEFI shell, Unified Kernel Image, etc.) as a boot option:

`sudo efibootmgr {{[-c|--create]}} {{[-d|--disk]}} {{/dev/sda}} {{[-p|--part]}} {{1}} {{[-l|--loader]}} "{{path\to\executable.efi}}" {{[-L|--label]}} "{{boot_entry_name}}"`

- Add Linux as a boot option:

`sudo efibootmgr {{[-c|--create]}} {{[-d|--disk]}} {{/dev/sda}} {{[-p|--part]}} {{1}} {{[-l|--loader]}} "{{path\to\vmlinuz}}" {{[-u|--unicode]}} "{{root=UUID=partition_uuid rw loglevel=3 initrd=path\to\initramfs-linux.img}}" {{[-L|--label]}} "{{Linux}}"`

- Change the current boot order:

`sudo efibootmgr {{[-o|--bootorder]}} {{0002,0008,0001,001A,...}}`

- Delete a boot option:

`sudo efibootmgr {{[-B|--delete-bootnum]}} {{[-b|--bootnum]}} {{0008}}`
