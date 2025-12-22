# az disk

> 管理 Azure 托管磁盘。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/disk>.

- 创建一个托管磁盘：

`az disk create {{[-g|--resource-group]}} {{资源组}} {{[-n|--name]}} {{磁盘名称}} {{[-z|--size-gb]}} {{大小（GB）}}`

- 列出资源组中的托管磁盘：

`az disk list {{[-g|--resource-group]}} {{资源组}}`

- 删除一个托管磁盘：

`az disk delete {{[-g|--resource-group]}} {{资源组}} {{[-n|--name]}} {{磁盘名称}}`

- 为托管磁盘授予读取或写入访问权限（用于导出）：

`az disk grant-access {{[-g|--resource-group]}} {{资源组}} {{[-n|--name]}} {{磁盘名称}} {{[--access|--access-level]}} {{读取|写入}} --duration-in-seconds {{秒数}}`

- 更新磁盘大小：

`az disk update {{[-g|--resource-group]}} {{资源组}} {{[-n|--name]}} {{磁盘名称}} {{[-z|--size-gb]}} {{新的大小（GB）}}`
