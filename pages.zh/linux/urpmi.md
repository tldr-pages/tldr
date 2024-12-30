# urpmi

> 在Mageia中安装软件包。
> 另请参阅：`urpm.update`、`urpme`、`urpmi.addmedia`、`urpmi.removemedia`、`urpmf`、`urpmq`。
> 更多信息：<https://wiki.mageia.org/en/URPMI#urpmi>。

- 从软件库或本地RPM文件安装软件包：

`sudo urpmi {{package|path/to/file.rpm}}`

- 下载软件包而不安装：

`urpmi --no-install {{package}}`

- 更新所有已安装的软件包（运行 `urpmi.update -a` 以获取可用更新）：

`sudo urpmi --auto-select`

- 根据 `/etc/urpmi/parallel.cfg` 在网络上的一台或多台机器上更新软件包：

`sudo urpmi --parallel local {{package}}`

- 将所有孤立软件包标记为手动安装：

`sudo urpmi $(urpmq --auto-orphans -f)`