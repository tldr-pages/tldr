# urpmi.update

> 更新Mageia中软件包仓库的包列表。
> 注意：Mageia文档中“medium”和“repository”是同义词。
> 另见：`urpmi`，`urpme`，`urpmi.addmedia`，`urpmi.removemedia`，`urpmf`，`urpmq`。
> 更多信息：<https://wiki.mageia.org/en/URPMI#urpmi.update>。

- 更新所有启用的媒体：

`urpmi.update -a`

- 更新特定的媒体（包括禁用的媒体）：

`urpmi.update {{medium1 medium2 ...}}`

- 更新所有包含特定关键字的媒体：

`urpmi.update {{keyword}}`

- 更新所有配置的媒体：

`urpmi.update e`