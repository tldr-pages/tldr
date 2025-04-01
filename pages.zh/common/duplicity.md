# duplicity

> 创建增量、压缩、加密和版本化备份。
> 还可以将备份上传到多种后端服务。
> 值得一提的是，根据版本不同，某些选项可能不可用（例如，在 2.0.0 版本中 `--gio` 选项不可用）。
> 更多信息：<https://duplicity.gitlab.io/stable/duplicity.1.html#name>。

- 通过 FTPS 备份目录到远程机器，使用密码加密：

`FTP_PASSWORD={{ftp_login_password}} PASSPHRASE={{encryption_password}} duplicity {{path/to/source/directory}} {{ftps://user@hostname/target/directory/path/}}`

- 将目录备份到 Amazon S3，每月进行一次完全备份：

`duplicity --full-if-older-than {{1M}} s3://{{bucket_name[/prefix]}}`

- 从 WebDAV 共享中删除超过 1 年的备份版本：

`FTP_PASSWORD={{webdav_login_password}} duplicity remove-older-than {{1Y}} --force {{webdav[s]://user@hostname[:port]/some_dir}}`

- 列出可用的备份：

`duplicity collection-status "file://{{absolute/path/to/backup/directory}}"`

- 通过 SSH 列出远程机器中存储的备份文件：

`duplicity list-current-files {{[-t|--time]}} {{YYYY-MM-DD}} scp://{{user@hostname}}/{{path/to/backup/dir}}`

- 从 GnuPG 加密的本地备份中恢复子目录到指定位置：

`PASSPHRASE={{gpg_key_password}} duplicity restore --encrypt-key {{gpg_key_id}} --path-to-restore {{relative/path/restoredirectory}} file://{{absolute/path/to/backup/directory}} {{path/to/directory/to/restore/to}}`
