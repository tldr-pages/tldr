# sfill

> Secure overwrite free space and inodes of the partition where the specified directory resides.
> More information: <https://manned.org/sfill>.

- Overwrite free space and inodes of an USB with 38 writes (slow but secure):

`sfill {{/media/user/mounted_usb_directory}}`

- Overwrite free space and inodes of an USB with 2 writes (fast but less secure) and show status:

`sfill -l -v {{/media/user/mounted_usb_directory}}`

- Overwrite only free spece of an USB:

`sfill -I {{/media/user/mounted_usb_directory}}`

- Overwrite only free inodes of an USB:

`sfill -i {{/media/user/mounted_usb_directory}}`
