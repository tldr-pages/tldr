# rpmconf

> 处理因软件包升级而遗留的 RPMNEW、RPMSAVE 和 RPMORIG 文件。
> 另见：`rpm`。
> 更多信息：<https://github.com/xsuchy/rpmconf>。

- 列出遗留文件并交互式选择对每个文件的处理方式：

`sudo rpmconf --all`

- 删除孤立的 RPMNEW 和 RPMSAVE 文件：

`sudo rpmconf --all --clean`