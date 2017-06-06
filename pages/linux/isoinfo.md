# isoinfo

> Utility programs for dumping and verifying iso images.

- List all the files packed into an iso:

`isoinfo -f -i {{path/to/image.iso}}`

- Extract a specific file to stdout:

`isoinfo -i {{path/to/image.iso}} -x {{/PATH/TO/FILE/INSIDE/ISO.EXT}}`

- Show header information for an iso:

`isoinfo -d -i {{path/to/image.iso}}`
