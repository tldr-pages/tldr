# chmod

> Change the permission of a file or directory

- Give the user (owner) rights to execute a file/directory

`chmod u+x {{file}}`

- Give the user (owner) rights to read and write to a file/directory

`chmod u+wr {{file}}`

- Change a file/directory to be readable/writable/executable for user (owner) and group, but only readable/executable for everyone else

`chmod 775 {{file}}`

- Change a file/directory to be readable/writable/executable for user (owner), but deny group and other (everyone else) read, write and execution rights.

`chmod 700 {{file}}`

- Change a file/directory to be readable/writable/executable for user (owner) and readable by group and other, but deny group and other (everyone else) write and execution rights.

`chmod 744 {{file}}`