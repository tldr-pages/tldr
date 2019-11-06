# mount

> Mount Network File System (NFS) network shares.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/mount>.

- Mount a share to the "Z" drive letter:

`mount \\{{computer_name}}\{{share_name}} {{Z:}}`

- Mount a share to the next available drive letter:

`mount \\{{computer_name}}\{{share_name}} *`

- Mount a share with a timeout in seconds:

`mount -o timeout={{seconds}} \\{{computer_name}}\{{share_name}} {{Z:}}`

- Mount a share and retry up to 10 times if it fails:

`mount -o retry={{retries}} \\{{computer_name}}\{{share_name}} {{Z:}}`

- Mount a share with forced case sensitivity:

`mount -o casesensitive \\{{computer_name}}\{{share_name}} {{Z:}}`

- Mount a share as an anonymous user:

`mount -o anon \\{{computer_name}}\{{share_name}} {{Z:}}`

- Mount a share using a specific mount type:

`mount -o mtype={{soft|hard}} \\{{computer_name}}\{{share_name}} {{Z:}}`
