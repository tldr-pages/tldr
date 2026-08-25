# kioclient

> Perform network-transparent file operations using KDE's KIO subsystem.
> Supports URL schemes such as `file:`, `sftp:`, `smb:`, `fish:`, and `trash:`.
> More information: <https://manned.org/kioclient>.

- Open a URL with its default KDE handler:

`kioclient exec {{url}}`

- Print the contents of a remote file to `stdout`:

`kioclient cat {{sftp://user@host/path/to/file}}`

- List the contents of a remote directory:

`kioclient ls {{smb://server/share}}`

- Copy one or more files via KIO:

`kioclient cp {{path/to/source1 path/to/source2 ...}} {{path/to/destination}}`

- Move a file via KIO:

`kioclient mv {{path/to/source}} {{path/to/destination}}`

- Remove a file via KIO:

`kioclient rm {{url}}`

- Create a new directory via KIO:

`kioclient mkdir {{url}}`

- Display help:

`kioclient --help`
