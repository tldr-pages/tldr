# transcrypt

> 在 Git 仓库中透明地加密文件。
> 更多信息请访问: <https://github.com/elasticdog/transcrypt>。

- 初始化一个未配置的仓库：

`transcrypt`

- 列出当前已加密的文件：

`git ls-crypt`

- 显示已配置仓库的凭据：

`transcrypt --display`

- 初始化并解密已配置仓库的新克隆：

`transcrypt --cipher={{cipher}}`

- 更改加密算法或密码：

`transcrypt --rekey`