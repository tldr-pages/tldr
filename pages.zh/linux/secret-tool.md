# secret-tool

> 存储和检索密码，是 `libsecret` 包的一部分。
> 与 Freedesktop 密钥服务实现（如 `gnome-keyring`）进行通信。
> 更多信息：<https://gnome.pages.gitlab.gnome.org/libsecret/>.

- 存储一个带有可选标签的秘密：

`secret-tool store --label={{label}} {{key}} {{value}}`

- 检索一个秘密：

`secret-tool lookup key {{key}}`

- 获取关于一个秘密的更多信息：

`secret-tool search key {{key}}`

- 删除一个已存储的秘密：

`secret-tool clear key {{key}}`