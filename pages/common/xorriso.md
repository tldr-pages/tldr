# xorriso

> Create, load, manipulate, and write ISO 9660 filesystem images.
> See also: `mkisofs`, `grub-mkrescue`.
> More information: <https://www.gnu.org/software/xorriso/man_1_xorriso.html>.

- Create an ISO image from a directory:

`xorriso -outdev {{path/to/image.iso}} -map {{path/to/directory}} /`

- Create an ISO image with a volume label using `mkisofs`-compatible options:

`xorriso -as mkisofs -o {{path/to/image.iso}} -V {{label}} -J -R {{path/to/directory}}`

- List files in the root directory of an ISO image:

`xorriso -indev {{path/to/image.iso}} -ls /`

- Find all files in an ISO image matching a pattern:

`xorriso -indev {{path/to/image.iso}} -find / -name '{{*.txt}}'`

- Extract all files from an ISO image to a directory:

`xorriso -osirrox on -indev {{path/to/image.iso}} -extract / {{path/to/output_directory}}`

- Extract a single file from an ISO image:

`xorriso -osirrox on -indev {{path/to/image.iso}} -extract /{{path/to/file}} {{path/to/output_file}}`

- Add a file to an existing ISO image:

`xorriso -dev {{path/to/image.iso}} -map {{path/to/file}} /{{path/in/image}}`

- Show the table of contents (sessions and size) of an ISO image or disc:

`xorriso -indev {{path/to/image.iso|/dev/sr0}} -toc`
