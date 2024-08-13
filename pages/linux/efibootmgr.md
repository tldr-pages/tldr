# efibootmgr

> Manipulate the UEFI Boot Manager.
> More information: <https://manned.org/efibootmgr>.

- List all boot options with their numbers:

`efibootmgr {{-u|--unicode}}`

- Add UEFI Shell v2 as a boot option:

`sudo efibootmgr -c -d {{/dev/sda}} -p {{1}} -l "{{\path\to\shell.efi}}" -L "{{UEFI Shell}}"`

- Add Linux as a boot option:

`sudo efibootmgr --create --disk {{/dev/sda}} --part {{1}} --loader "{{\vmlinuz}}" --unicode "{{kernel_cmdline}}" --label "{{Linux}}"`

- Change the current boot order:

`sudo efibootmgr {{-o|--bootorder}} {{0002,0008,0001,0005}}`

- Delete a boot option:

`sudo efibootmgr {{-b|--bootnum}} {{0008}} {{-B|--delete-bootnum}}`
