# duplicity

> Create incremental, compressed, encrypted and versioned backups.
> Can also upload the backups to a variety of backend services.
> It is worth mentioning that depending on the version, some options may not be available (e.g. `--gio` in 2.0.0).
> More information: <https://duplicity.gitlab.io/stable/duplicity.1.html#name>.

- Backup a directory via FTPS to a remote machine, encrypting it with a password:

`FTP_PASSWORD={{ftp_login_password}} PASSPHRASE={{encryption_password}} duplicity {{path/to/source_directory}} {{ftps://user@hostname/path/to/target_directory}}/`

- Backup a directory to Amazon S3, doing a full backup every month:

`duplicity --full-if-older-than {{1M}} s3://{{bucket_name[/prefix]}}`

- Delete versions older than 1 year from a backup stored on a WebDAV share:

`FTP_PASSWORD={{webdav_login_password}} duplicity remove-older-than {{1Y}} --force {{webdav[s]://user@hostname[:port]/some_directory}}`

- List the available backups:

`duplicity collection-status "file://{{absolute/path/to/backup_directory}}"`

- List the files in a backup stored on a remote machine, via SSH:

`duplicity list-current-files {{[-t|--time]}} {{YYYY-MM-DD}} scp://{{user@hostname}}/{{path/to/backup_directory}}`

- Restore a subdirectory from a GnuPG-encrypted local backup to a given location:

`PASSPHRASE={{gpg_key_password}} duplicity restore --encrypt-key {{gpg_key_id}} --path-to-restore {{path/to/restore_directory}} file://{{absolute/path/to/backup_directory}} {{path/to/directory_to_restore_to}}`
