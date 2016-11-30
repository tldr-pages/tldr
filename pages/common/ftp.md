# ftp

> Internet File Transfer Protocol

- Connect to a FTP server:

`ftp {{ftp.example.com}}`

- Switch to binary transfer mode (graphics, compressed files etc):

`binary`

- Turn off interactive prompting for multiple file transfers:

`prompt off`

- Download multiple files (glob expression):

`mget {{*.png}}`

- Upload multiple files (glob expression):

`mput {{*.zip}}`

- Delete multiple files on the remote machine (glob expression):

`mdelete {{*.txt}}`
