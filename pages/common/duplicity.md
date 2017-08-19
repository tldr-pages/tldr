# duplicity

> Creates incremental, compressed, encrypted and versioned backups and optionally uploads them to a variety of backend services.

- Backup a folder via ftps to a remote machine, encrypting with a password:

`FTP_PASSWORD={{ftp_login_password}} PASSPHRASE={{encryption_password}} duplicity {{path/to/source/directory}} {{ftps://user@hostname/target/directory/path/}}`

- Backup a folder to Amazon S3, doing a full backup every month:

`duplicity --full-if-older-than {{1M}} --use-new-style s3://{{bucket_name[/prefix]}}`

- Delete versions older than 1 year from a backup stored on a webdav share:

`FTP_PASSWORD={{webdav_login_password}} duplicity remove-older-than {{1Y}} --force {{webdav[s]://user@hostname[:port]/some_dir}}`

- List the backups available:

`duplicity collection-status "file://{{absolute/path/to/backup/folder}}"`

- List the files in a backup stored on a remote machine via ssh:

`duplicity list-current-files --time {{YYYY-MM-DD}} scp://{{user@hostname}}/path/to/backup/dir`

- Restore a folder from a gpg-encrypted local backup to a folder:

`PASSPHRASE={{gpg_key_password}} duplicity restore --encrypt-key {{gpg_key_id}} --file-to-restore {{relative/path/restorefolder}} file://{{absolute/path/to/backup/folder}} {{path/to/directory/to/restore/to}}`
