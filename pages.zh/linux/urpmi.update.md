# urpmi.update

> 更新 Mageia 中软件包仓库的软件包列表。
> 注意：Mageia 文档中“介质”和“仓库”是同义词。
> 参见：`urpmi`、`urpme`、`urpmi.addmedia`、`urpmi.removemedia`、`urpmf`、`urpmq`。
> 更多信息：<https://wiki.mageia.org/en/URPMI#urpmi.update>。

- 更新所有已启用的介质：

`urpmi.update -a`

- 更新特定的介质（包括已禁用的介质）：

`urpmi.update {{medium1 medium2 ...}}`

- 更新包含特定关键字的所有介质：

`urpmi.update {{keyword}}`

- 更新所有已配置的介质：

`urpmi.update e`
