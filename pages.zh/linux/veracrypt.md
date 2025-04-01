# veracrypt

> 免费且开源的磁盘加密软件。
> 更多信息：<https://www.veracrypt.fr/code/VeraCrypt/plain/doc/html/Documentation.html>.

- 通过文本用户界面创建新卷并使用 `/dev/urandom` 作为随机数据源：

`veracrypt --text --create --random-source={{/dev/urandom}}`

- 通过文本用户界面交互式解密卷并挂载到目录：

`veracrypt --text {{path/to/volume}} {{path/to/mount_point}}`

- 使用密钥文件解密分区并挂载到目录：

`veracrypt --keyfiles={{path/to/keyfile}} {{/dev/sdXN}} {{path/to/mount_point}}`

- 卸载已经挂载到目录的卷：

`veracrypt --dismount {{path/to/mounted_point}}`