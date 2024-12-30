# aurvote

> 为 Arch 用户库中的软件包投票。
> 要能够投票，文件 `~/.config/aurvote` 必须存在并包含您的 AUR 凭据。
> 更多信息：<https://github.com/archlinuxfr/aurvote>。

- 交互式创建文件 `~/.config/aurvote`，其中包含您的 AUR 用户名和密码：

`aurvote --configure`

- 为一个或多个 AUR 软件包投票：

`aurvote {{package1 package2 ...}}`

- 撤销对一个或多个 AUR 软件包的投票：

`aurvote --unvote {{package1 package2 ...}}`

- 检查一个或多个 AUR 软件包是否已被投票：

`aurvote --check {{package1 package2 ...}}`

- 显示帮助信息：

`aurvote --help`