# xorriso

> Create, load, manipulate and write ISO 9660 filesystem images.
> More information: <https://manned.org/xorriso>.

- Create an ISO image from a directory:

`xorriso -outdev {{path/to/image.iso}} -map {{path/to/source_directory}} /`

- Create an ISO image from multiple directories and set the volume ID:

`xorriso -outdev {{path/to/image.iso}} -volid "{{volume_name}}" -map {{path/to/directory1}} {{/directory1}} -map {{path/to/directory2}} {{/directory2}}`

- List all files in an ISO image:

`xorriso -indev {{path/to/image.iso}} -find /`

- Extract a directory from an ISO image:

`xorriso -osirrox on -indev {{path/to/image.iso}} -extract {{/path/inside_iso}} {{path/to/output_directory}}`

- Copy an ISO image, adding or removing files:

`xorriso -indev {{path/to/original.iso}} -outdev {{path/to/modified.iso}} -map {{path/to/file}} {{/path/inside_iso}} -rm_r {{/path/to/remove}} --`
