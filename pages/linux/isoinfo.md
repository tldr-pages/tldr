# isoinfo

> Utility programs for dumping and verifying ISO disk images.

- List all the files included in an ISO image:

`isoinfo -f -i {{path/to/image.iso}}`

- E[x]tract a specific file from an ISO image and send it out `stdout`:

`isoinfo -i {{path/to/image.iso}} -x {{/PATH/TO/FILE/INSIDE/ISO.EXT}}`

- Show header information for an ISO disk image:

`isoinfo -d -i {{path/to/image.iso}}`
