# lsb_release

> 获取 LSB（Linux 标准基础）和特定发行版的信息。
> 更多信息：<https://manned.org/lsb_release>。

- 打印所有可用信息：

`lsb_release -a`

- 打印操作系统的描述（通常是全名）：

`lsb_release -d`

- 仅打印操作系统名称（ID），并抑制字段名称：

`lsb_release -i -s`

- 打印发行版的版本号和代号，抑制字段名称：

`lsb_release -rcs`