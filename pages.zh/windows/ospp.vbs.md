# ospp.vbs

> 安装、激活和管理 Microsoft Office 产品的批量许可版本。
> 注意：此命令可能会覆盖、停用和/或移除您当前的 Office 产品批量许可版本，请谨慎操作。
> 更多信息：<https://learn.microsoft.com/deployoffice/vlactivation/tools-to-manage-volume-activation-of-office>.

- 安装产品密钥（注意：它将替换现有密钥）：

`cscript ospp.vbs /inpkey:{{product_key}}`

- 卸载已安装的产品密钥，使用产品密钥的最后五位数字：

`cscript ospp.vbs /unpkey:{{product_key_digits}}`

- 设置 KMS 主机名：

`cscript ospp.vbs /sethst:{{ip|hostname}}`

- 设置 KMS 端口：

`cscript ospp.vbs /setprt:{{port}}`

- 激活已安装的 Office 产品密钥：

`cscript ospp.vbs /act`

- 显示已安装产品密钥的许可信息：

`cscript ospp.vbs /dstatus`
