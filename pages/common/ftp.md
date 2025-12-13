# ftp

> Tools to interact with a server via File Transfer Protocol.
> More information: <https://manned.org/ftp>.

- Connect to an FTP server and run in interactive mode:

`ftp {{ftp.example.com}}`

- Connect to an FTP server specifying its IP address and port:

`ftp {{ip_address}} {{port}}`

- [Interactive] Switch to binary transfer mode (graphics, compressed files, etc):

`binary`

- [Interactive] Transfer multiple files without prompting for confirmation on every file:

`prompt off`

- [Interactive] Download multiple files (glob expression):

`mget {{*.png}}`

- [Interactive] Upload multiple files (glob expression):

`mput {{*.zip}}`

- [Interactive] Delete multiple files on the remote server:

`mdelete {{*.txt}}`

- [Interactive] Rename a file on the remote server:

`rename {{original_filename}} {{new_filename}}`
