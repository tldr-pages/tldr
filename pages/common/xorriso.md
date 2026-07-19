# xorriso

> Create, load, manipulate, and write ISO 9660 filesystem images.
> See also: `mkisofs`, `genisoimage`, `dd`.
> More information: <https://www.gnu.org/software/xorriso/man_1_xorriso.html>.

- Create an ISO image from a directory:

`xorriso -as mkisofs -o {{path/to/image.iso}} {{path/to/directory}}`

- List the contents of an ISO image:

`xorriso -indev {{path/to/image.iso}} -ls`

- Extract files from an ISO image to a directory:

`xorriso -osirrox on -indev {{path/to/image.iso}} -extract / {{path/to/directory}}`

- Add files to an existing ISO image and write a new image:

`xorriso -indev {{path/to/old.iso}} -outdev {{path/to/new.iso}} -map {{path/to/file}} {{/path/in/iso}} -commit`

- Write an ISO image to an optical drive:

`xorriso -as cdrecord -v dev={{/dev/sr0}} {{path/to/image.iso}}`

- Create a bootable ISO with an El Torito boot image:

`xorriso -as mkisofs -o {{path/to/image.iso}} -b {{isolinux/isolinux.bin}} -c {{boot.cat}} -no-emul-boot -boot-load-size 4 -boot-info-table {{path/to/directory}}`
