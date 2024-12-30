# veracrypt

> 免费和开源的磁盘加密软件。
> 更多信息：<https://www.veracrypt.fr/code/VeraCrypt/plain/doc/html/Documentation.html>。

- 通过文本用户界面创建一个新卷，并使用 `/dev/urandom` 作为随机数据源：

`veracrypt --text --create --random-source={{/dev/urandom}}`

- 通过文本用户界面交互式解密一个卷并将其挂载到一个目录：

`veracrypt --text {{path/to/volume}} {{path/to/mount_point}}`

- 使用密钥文件解密一个分区并将其挂载到一个目录：

`veracrypt --keyfiles={{path/to/keyfile}} {{/dev/sdXN}} {{path/to/mount_point}}`

- 卸载已挂载到目录的卷：

`veracrypt --dismount {{path/to/mounted_point}}`