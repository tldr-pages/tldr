# mmls

> Display the partition layout of a volume system.
> More information: <https://wiki.sleuthkit.org/index.php?title=Mmls>.

- Display the partition table stored in an image file:

`mmls {{imagefile}}`

- Display the partition table with an additional column for the partition size:

`mmls -B -i {{image}}`

- Display the partition table in a splitted EWF image:

`mmls -i ewf {{image.e01}} {{image.e02}}`

- Display nested partition tables:

`mmls -t {{nested_table_type}} -o {{offset}} {{image}}`
