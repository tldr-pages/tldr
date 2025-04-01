# transcrypt

> 在 Git 仓库中透明地加密文件。
> 更多信息：<https://github.com/elasticdog/transcrypt>.

- 初始化一个未配置的仓库：

`transcrypt`

- 列出当前加密的文件：

`git ls-crypt`

- 显示已配置仓库的凭据：

`transcrypt --display`

- 初始化并解密一个已配置仓库的新克隆：

`transcrypt --cipher={{cipher}}`

- 重新设置密钥以更改加密算法或密码：

`transcrypt --rekey`
