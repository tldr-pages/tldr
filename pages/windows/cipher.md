# cipher

> Display or alter the encryption of directories and files on NTFS volumes.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cipher>.

- Display information about a specific encrypted file or directory:

`cipher /c:{{path\to\file_or_directory}}`

- [e]ncrypt a file or directory (files added later to the directory are also encrypted as the directory is marked):

`cipher /e:{{path\to\file_or_directory}}`

- [d]ecrypt a file or directory:

`cipher /d:{{path\to\file_or_directory}}`

- Securely remove a file or directory:

`cipher /w:{{path\to\file_or_directory}}`
