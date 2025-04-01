# urpmi

> 在 Mageia 中安装软件包。
> 请参阅：`urpm.update`、`urpme`、`urpmi.addmedia`、`urpmi.removemedia`、`urpmf`、`urpmq`。
> 更多信息：<https://wiki.mageia.org/en/URPMI#urpmi>。

- 从仓库或本地 RPM 文件安装包：

`sudo urpmi {{package|path/to/file.rpm}}`

- 下载包但不安装：

`urpmi --no-install {{package}}`

- 更新所有已安装的包（运行 `urpmi.update -a` 以获取可用更新）：

`sudo urpmi --auto-select`

- 根据 `/etc/urpmi/parallel.cfg` 更新网络中一台或多台机器上的包：

`sudo urpmi --parallel local {{package}}`

- 将所有孤立包标记为手动安装：

`sudo urpmi $(urpmq --auto-orphans -f)`
