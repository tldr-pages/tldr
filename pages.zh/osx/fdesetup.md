# fdesetup

> 设置和检索与 FileVault 相关的信息。
> 更多信息：<https://keith.github.io/xcode-man-pages/fdesetup.8.html>。

- 列出当前启用 FileVault 的用户：

`sudo fdesetup list`

- 获取当前 FileVault 状态：

`fdesetup status`

- 添加启用 FileVault 的用户：

`sudo fdesetup add -usertoadd {{user1}}`

- 启用 FileVault：

`sudo fdesetup enable`

- 禁用 FileVault：

`sudo fdesetup disable`
