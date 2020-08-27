# tune2fs

> Adjust paramters of an ext2, ext3 or ext4 file system.

- Set the max number of counts before a file system is checked to 2:

`tune2fs -c {{2}} {{/dev/sda1}}`

- Set the file system label to MY_LABEL:

`tune2fs -L {{'MY_LABEL'}} {{/dev/sda1}}`

- Enable discard and user-specified extended attributes for a file system:

`tune2fs -o {{discard,user_xattr}} {{/dev/sda1}}`

- Enable journaling for a file system:

`tune2fs -o^{{nobarrier}} {{/dev/sda1}}`
