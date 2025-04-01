# urpme

> 卸载 Mageia 中的软件包。
> 参见: `urpmi`, `urpmi.update`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`。
> 更多信息: <https://wiki.mageia.org/en/URPMI#urpme>。

- 卸载一个软件包：

`sudo urpme {{package}}`

- 卸载孤儿软件包（注意：谨慎使用，可能会无意中删除重要软件包）：

`sudo urpme --auto-orphans`

- 卸载一个软件包及其依赖项：

`sudo urpme --auto-orphans {{package}}`
