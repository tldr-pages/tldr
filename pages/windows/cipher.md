# cipher

> Encrypt or decrypt files on NTFS drives.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cipher>.

- Encrypt a file or directory:

`cipher /e:{{path/to/file_or_directory}}`

- Decrypt a file or directory:

`cipher /d:{{path/to/file_or_directory}}`

- Securely remove a file or directory:

`cipher /w:{{path/to/file_or_directory}}`
