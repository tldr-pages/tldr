# scp

- Copies files between hosts on a network
- Works over a secure connection (SSH)

## Uploading a file

`scp local_file 10.0.0.1:/remote/path/filename`

## Uploading a directory

`scp -r local_folder 10.0.0.1:/remote/path/`

## Downloading a file

`scp 10.0.0.1:/remote/path/filename local_file`

## Specifying credentials

`scp local_file my_user@10.0.0.1:/remote/path`
