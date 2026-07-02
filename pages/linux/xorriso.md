# xorriso

> Create, load, manipulate and write ISO 9660 filesystem images with Rock Ridge extensions.
> More information: <https://manned.org/xorriso>.

- Create an ISO image from a directory:

`xorriso -as mkisofs -o {{path/to/output.iso}} {{path/to/directory}}`

- Create an ISO image with a volume label:

`xorriso -as mkisofs -o {{path/to/output.iso}} -V "{{label}}" {{path/to/directory}}`

- Create a bootable ISO image from a directory with an ISOLINUX boot loader:

`xorriso -as mkisofs -b {{isolinux/isolinux.bin}} -c {{isolinux/boot.cat}} -no-emul-boot -boot-load-size {{4}} -boot-info-table -o {{path/to/output.iso}} {{path/to/directory}}`

- List the files in an ISO image:

`xorriso -dev {{path/to/image.iso}} -ls {{/}}`

- Extract the contents of an ISO image into a directory:

`xorriso -dev {{path/to/image.iso}} -osirrox on -extract {{/}} {{path/to/directory}}`

- Burn files from a directory onto a blank disc:

`xorriso -dev {{/dev/sr0}} -blank as_needed -map {{path/to/directory}} / -- -commit`

- Blank a rewritable disc:

`xorriso -dev {{/dev/sr0}} -blank as_needed`
