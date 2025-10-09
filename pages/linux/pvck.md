# pvck

> Check and repair LVM metadata on physical volumes.
> More information: <https://manned.org/pvck>.

- Print LVM on-disk headers and structures (label, PV header, MDA header, metadata area):

`pvck --dump headers {{/dev/sdXN}}`

- Print the current VG metadata text:

`pvck --dump metadata {{/dev/sdXN}}`

- List all metadata versions found in the metadata area:

`pvck --dump metadata_all {{/dev/sdXN}}`

- Search common locations for metadata when headers may be damaged, and save it to a file:

`pvck --dump metadata_search {{[-f|--file]}} {{path/to/metadata.txt}} {{/dev/sdXN}}`

- Select the second metadata area (mda2) when printing metadata:

`pvck --dump metadata --settings "mda_num=2" {{/dev/sdXN}}`

- Repair headers and metadata using a metadata input file (use with care):

`pvck --repair {{[-f|--file]}} {{path/to/metadata_file}} {{/dev/sdXN}}`

- Repair only the PV header and label header:

`pvck --repairtype pv_header {{/dev/sdXN}}`
