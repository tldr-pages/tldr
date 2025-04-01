# systemd-tmpfiles

> 创建、删除和清理易失性和临时文件及目录。
> 该命令在启动时由 systemd 服务自动调用，通常不需要手动运行。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-tmpfiles.html>。

- 根据配置创建文件和目录：

`systemd-tmpfiles --create`

- 根据配置的年龄参数清理文件和目录：

`systemd-tmpfiles --clean`

- 根据配置删除文件和目录：

`systemd-tmpfiles --remove`

- 应用用户特定配置的操作：

`systemd-tmpfiles --create --user`

- 执行标记为早期启动的行：

`systemd-tmpfiles --create --boot`