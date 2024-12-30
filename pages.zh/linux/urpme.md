# urpme

> 在Mageia中卸载软件包。
> 另见：`urpmi`、`urpmi.update`、`urpmi.addmedia`、`urpmi.removemedia`、`urpmf`、`urpmq`。
> 更多信息：<https://wiki.mageia.org/en/URPMI#urpme>。

- 卸载一个软件包：

`sudo urpme {{package}}`

- 卸载孤儿软件包（注意：请谨慎使用，因为这可能会意外卸载重要的软件包）：

`sudo urpme --auto-orphans`

- 卸载一个软件包及其依赖项：

`sudo urpme --auto-orphans {{package}}`