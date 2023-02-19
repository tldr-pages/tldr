# lftp

> Sophisticated file transfer program.
> More information: <https://lftp.yar.ru/lftp-man.html>.

- Connect to an FTP server:

`lftp --user {{username}} {{ftp.example.com}}`

- Download multiple files (glob expression):

`mget {{path/to/*.png}}`

- Upload multiple files (glob expression):

`mput {{path/to/*.zip}}`

- Delete multiple files on the remote server:

`mrm {{path/to/*.txt}}`

- Rename a file on the remote server:

`mv {{original_filename}} {{new_filename}}`

- Download or update an entire directory:

`mirror {{path/to/remote_dir}} {{path/to/local_output_dir}}`

- Upload or update an entire directory:

`mirror -R {{path/to/local_dir}} {{path/to/remote_output_dir}}`
