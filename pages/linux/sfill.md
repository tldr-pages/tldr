# sfill

> Securely overwrite the free space and inodes of the partition where the specified directory resides.
> More information: <https://manned.org/sfill>.

- Overwrite free space and inodes of a disk with 38 writes (slow but secure):

`sfill {{/path/to/mounted_disk_directory}}`

- Overwrite free space and inodes of a disk with 6 writes (fast but less secure) and show status:

`sfill -l -v {{/path/to/mounted_disk_directory}}`

- Overwrite free space and inodes of a disk with 1 write (very fast but insecure) and show status:

`sfill -ll -v {{/path/to/mounted_disk_directory}}`

- Overwrite only free space of a disk:

`sfill -I {{/path/to/mounted_disk_directory}}`

- Overwrite only free inodes of a disk:

`sfill -i {{/path/to/mounted_disk_directory}}`
