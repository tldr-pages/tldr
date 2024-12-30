# duplicity

> 创建增量、压缩、加密和版本化的备份。
> 还可以将备份上传到各种后端服务。
> 值得一提的是，某些选项可能会根据版本的不同而不可用（例如，2.0.0中的`--gio`）。
> 更多信息：<https://duplicity.gitlab.io>。

- 通过FTPS将目录备份到远程机器，并使用密码进行加密：

`FTP_PASSWORD={{ftp_login_password}} PASSPHRASE={{encryption_password}} duplicity {{path/to/source/directory}} {{ftps://user@hostname/target/directory/path/}}`

- 每月对Amazon S3进行完整备份：

`duplicity --full-if-older-than {{1M}} s3://{{bucket_name[/prefix]}}`

- 从存储在WebDAV共享上的备份中删除超过1年的版本：

`FTP_PASSWORD={{webdav_login_password}} duplicity remove-older-than {{1Y}} --force {{webdav[s]://user@hostname[:port]/some_dir}}`

- 列出可用的备份：

`duplicity collection-status "file://{{absolute/path/to/backup/directory}}"`

- 列出存储在远程机器上的备份中的文件，通过SSH：

`duplicity list-current-files --time {{YYYY-MM-DD}} scp://{{user@hostname}}/{{path/to/backup/dir}}`

- 从GnuPG加密的本地备份中恢复子目录到指定位置：

`PASSPHRASE={{gpg_key_password}} duplicity restore --encrypt-key {{gpg_key_id}} --path-to-restore {{relative/path/restoredirectory}} file://{{absolute/path/to/backup/directory}} {{path/to/directory/to/restore/to}}`