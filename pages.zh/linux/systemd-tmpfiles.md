# systemd-tmpfiles

> 创建、删除和清理易失性和临时文件及目录。
> 此命令由systemd服务在启动时自动调用，通常不需要手动运行。
> 更多信息: <https://www.freedesktop.org/software/systemd/man/systemd-tmpfiles.html>。

- 按照配置创建文件和目录：

`systemd-tmpfiles --create`

- 清理具有配置的时间参数的文件和目录：

`systemd-tmpfiles --clean`

- 按照配置删除文件和目录：

`systemd-tmpfiles --remove`

- 应用用户特定配置的操作：

`systemd-tmpfiles --create --user`

- 执行标记为早期启动的行：

`systemd-tmpfiles --create --boot`