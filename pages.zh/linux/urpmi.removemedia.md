# urpmi.removemedia

> 移除 Mageia 中的介质。
> 注意：Mageia 文档中将介质和仓库视为同义词。
> 参见：`urpmi`，`urpme`，`urpmi.addmedia`，`urpmi.update`，`urpmf`，`urpmq`。
> 更多信息：<https://wiki.mageia.org/en/URPMI#urpmi.removemedia>。

- 移除一个介质：

`sudo urpmi.removemedia {{medium}}`

- 移除所有介质：

`sudo urpmi.removemedia -a`

- 根据介质名称的模糊匹配移除介质：

`sudo urpmi.removemedia -y {{keyword}}`