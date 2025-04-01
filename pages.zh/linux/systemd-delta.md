# systemd-delta

> 查找被覆盖的 systemd 相关配置文件。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-delta.html>.

- 显示所有被覆盖的配置文件：

`systemd-delta`

- 显示特定类型（以逗号分隔的列表）的文件：

`systemd-delta --type {{masked|equivalent|redirected|overridden|extended|unchanged}}`

- 显示路径以指定前缀开头的文件（注意：前缀是一个包含 systemd 配置文件子目录的目录）：

`systemd-delta {{/etc|/run|/usr/lib|...}}`

- 通过添加后缀进一步限制搜索路径（前缀是可选的）：

`systemd-delta {{prefix}}/{{tmpfiles.d|sysctl.d|systemd/system|...}}`