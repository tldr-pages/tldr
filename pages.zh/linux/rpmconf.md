# rpmconf

> 处理软件包升级后留下的 RPMNEW、RPMSAVE 和 RPMORIG 文件。
> 参见：`rpm`。
> 更多信息： <https://github.com/xsuchy/rpmconf>.

- 列出剩余文件并交互式地选择如何处理每个文件：

`sudo rpmconf --all`

- 删除孤立的 RPMNEW 和 RPMSAVE 文件：

`sudo rpmconf --all --clean`
