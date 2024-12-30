# urpmi.addmedia

> 在Mageia中添加媒体。
> 注意：Mageia文档使用medium和repository作为同义词。
> 另见：`urpmi`，`urpmi.update`，`urpme`，`urpmi.removemedia`，`urpmf`，`urpmq`。
> 更多信息：<https://wiki.mageia.org/en/URPMI#urpme>。

- 添加一个媒体：

`sudo urpmi.addmedia {{medium}} {{ftp://ftp.site.com/path/to/Mageia/RPMS}}`

- 从硬盘添加媒体（首先在目录中运行`genhdlist2`）：

`sudo urpmi.addmedia --distrib HD file:/{{/path/to/repo}}`

- 从所选镜像添加重要媒体：

`sudo urpmi.addmedia --distrib ftp://{{mirror_website}}/mirror/mageia/distrib/{{version}}/{{arch}}`

- 从镜像列表中自动选择镜像：

`sudo urpmi.addmedia --distrib --mirrorlist {{mirrorlist}}`