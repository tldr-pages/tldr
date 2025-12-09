# aurvote

> 为 AUR 中的包投票。
> 为了投票成功，文件 `~/.config/aurvote` 必须存在并包含你的 AUR 身份凭证。
> 更多信息：<https://github.com/archlinuxfr/aurvote#name>.

- 交互式创建包含你的 AUR 用户名和密码的 `~/.config/aurvote` 文件：

`aurvote --configure`

- 为一个或多个 AUR 包投票：

`aurvote {{package1 package2 ...}}`

- 为一个或多个 AUR 包取消投票：

`aurvote --unvote {{package1 package2 ...}}`

- 检查一个或多个 AUR 包是否已投票：

`aurvote --check {{package1 package2 ...}}`

- 查看 `aurvote` 的帮助信息：

`aurvote --help`
