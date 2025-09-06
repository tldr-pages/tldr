# airshare

> Transfer data between two machines in a local network.
> More information: <https://airshare.rtfd.io/en/latest/cli.html>.

- Share files or directories:

`airshare {{code}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Receive a file:

`airshare {{code}}`

- Host a receiving server (use this to be able to upload files using the web interface):

`airshare --upload {{code}}`

- Send files or directories to a receiving server:

`airshare --upload {{code}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Send files whose paths have been copied to the clipboard:

`airshare --file-path {{code}}`

- Receive a file and copy it to the clipboard:

`airshare --clip-receive {{code}}`
