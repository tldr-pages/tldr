# lftp

> Sophisticated file transfer program.

- Connect to an FTP server:

`lftp {{ftp.example.com}}`

- Download multiple files (glob expression):

`mget {{*.png}}`

- Upload multiple files (glob expression):

`mput {{*.zip}}`

- Delete multiple files on the remote server:

`mrm {{*.txt}}`

- Rename a file on the remote server:

`mv {{original_filename}} {{new_filename}}`

- Download or update an entire directory:

`mirror {{remote_dir/}} {{local_output_dir/}}`

- Upload or update an entire directory:

`mirror -R {{local_dir/}} {{remote_output_dir/}}`
