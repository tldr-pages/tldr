# urpmi.addmedia

> 在 Mageia 中添加介质。
> 注意：Mageia 文档中 “介质” 和 “仓库” 是同义词。
> 另见：`urpmi`、`urpmi.update`、`urpme`、`urpmi.removemedia`、`urpmf`、`urpmq`。
> 更多信息：<https://wiki.mageia.org/en/URPMI#urpme>。

- 添加介质：

`sudo urpmi.addmedia {{medium}} {{ftp://ftp.site.com/path/to/Mageia/RPMS}}`

- 从硬盘添加介质（首先在目录中运行 `genhdlist2`）：

`sudo urpmi.addmedia --distrib HD file:/{{/path/to/repo}}`

- 从选定的镜像添加重要介质：

`sudo urpmi.addmedia --distrib ftp://{{mirror_website}}/mirror/mageia/distrib/{{version}}/{{arch}}`

- 从镜像列表中自动选择镜像：

`sudo urpmi.addmedia --distrib --mirrorlist {{mirrorlist}}`