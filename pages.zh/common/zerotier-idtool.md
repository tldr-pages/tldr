# zerotier-idtool

> 创建和操作 ZeroTier 身份。
> 更多信息：<https://github.com/zerotier/ZeroTierOne/blob/dev/doc/zerotier-idtool.1.md>。

- 生成一个新的 ZeroTier 身份，并将私钥部分输出到 `stdout`：

`zerotier-idtool generate`

- 生成一个新的 ZeroTier 身份，并将私钥和公钥部分保存到文件中：

`zerotier-idtool generate {{路径/到/identity.secret}} {{路径/到/identity.public}}`

- 生成一个具有指定十六进制靓号前缀的 ZeroTier 身份（可能需要很长时间）：

`zerotier-idtool generate {{路径/到/identity.secret}} {{路径/到/identity.public}} {{靓号_前缀}}`

- 从私钥身份中提取公钥部分：

`zerotier-idtool getpublic {{路径/到/identity.secret}}`

- 使用私钥身份对文件进行签名：

`zerotier-idtool sign {{路径/到/identity.secret}} {{路径/到/文件}}`

- 使用公钥身份和一个十六进制签名来验证已签名的文件：

`zerotier-idtool verify {{路径/到/identity.public}} {{路径/到/文件}} {{签名_十六进制}}`

- 在本地验证一个身份的密钥和工作量证明：

`zerotier-idtool validate {{路径/到/identity.public}}`

- 显示帮助：

`zerotier-idtool help`
