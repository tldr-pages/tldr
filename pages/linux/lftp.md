# lftp

> Sophisticated file transfer program.
> More information: <https://lftp.yar.ru/lftp-man.html>.

- Connect to an FTP server:

`lftp {{[-u|--user]}} {{username}} {{ftp.example.com}}`

- [Interactive] Download multiple files (glob expression):

`mget {{path/to/*.png}}`

- [Interactive] Upload multiple files (glob expression):

`mput {{path/to/*.zip}}`

- [Interactive] Delete multiple files on the remote server:

`mrm {{path/to/*.txt}}`

- [Interactive] Rename a file on the remote server:

`mv {{original_filename}} {{new_filename}}`

- [Interactive] Download or update an entire directory:

`mirror {{path/to/remote_directory}} {{path/to/local_output_directory}}`

- [Interactive] Upload or update an entire directory:

`mirror {{[-R|--reverse]}} {{path/to/local_directory}} {{path/to/remote_output_directory}}`
