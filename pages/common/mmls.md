# mmls

> Display the partition layout of a volume system.
> More information: <https://github.com/sleuthkit/sleuthkit/wiki/mmls>.

- Display the partition table stored in an image file:

`mmls {{path/to/image_file}}`

- Display the partition table with an additional column for the partition size:

`mmls -B -i {{path/to/image_file}}`

- Display the partition table in a split EWF image:

`mmls -i ewf {{image.e01}} {{image.e02}}`

- Display nested partition tables:

`mmls -t {{nested_table_type}} -o {{offset}} {{path/to/image_file}}`
