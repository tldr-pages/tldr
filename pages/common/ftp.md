# ftp

> Tools to interact with a server via File Transfer Protocol.
> More information: <https://manned.org/ftp>.

- Connect to an FTP server:

`ftp {{ftp.example.com}}`

- Connect to an FTP server specifying its IP address and port:

`ftp {{ip_address}} {{port}}`

- Switch to binary transfer mode (graphics, compressed files, etc):

`binary`

- Transfer multiple files without prompting for confirmation on every file:

`prompt off`

- Download multiple files (glob expression):

`mget {{*.png}}`

- Upload multiple files (glob expression):

`mput {{*.zip}}`

- Delete multiple files on the remote server:

`mdelete {{*.txt}}`

- Rename a file on the remote server:

`rename {{original_filename}} {{new_filename}}`
