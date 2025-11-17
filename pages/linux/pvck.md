# pvck

> Check and repair LVM metadata on physical volumes.
> More information: <https://manned.org/pvck>.

- Print LVM on-disk headers and structures (label, PV header, MDA header, metadata area):

`sudo pvck {{/dev/sdXN}} --dump headers`

- Print the current VG metadata text:

`sudo pvck {{/dev/sdXN}} --dump metadata`

- List all metadata versions found in the metadata area:

`sudo pvck {{/dev/sdXN}} --dump metadata_all`

- Search common locations for metadata when headers may be damaged, and save it to a file:

`sudo pvck {{/dev/sdXN}} --dump metadata_search {{[-f|--file]}} {{path/to/metadata.txt}}`

- Select the second metadata area (mda2) when printing metadata:

`sudo pvck {{/dev/sdXN}} --dump metadata --settings "mda_num=2"`

- Repair headers and metadata using a metadata input file (use with care):

`sudo pvck {{/dev/sdXN}} --repair {{[-f|--file]}} {{path/to/metadata_file}}`

- Repair only the PV header and label header:

`sudo pvck {{/dev/sdXN}} --repairtype pv_header`
