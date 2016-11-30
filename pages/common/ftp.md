# ftp

> Tools to interact with a server via File Transfer Protocol.

- Connect to an FTP server:

`ftp {{ftp.example.com}}`

- Switch to binary transfer mode (graphics, compressed files, etc):

`binary`

- Turn off interactive prompting for multiple file transfers:

`prompt off`

- Download multiple files (glob expression):

`mget {{*.png}}`

- Upload multiple files (glob expression):

`mput {{*.zip}}`

- Delete a single file on the remote server:

`delete {{filename}}`

- Rename a file on the remove server:

`rename {{original_filename}} {{new_filename}}`
