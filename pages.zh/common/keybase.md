# keybase

> 一个密钥目录，将社交媒体身份映射到加密密钥，以公开可审计的方式进行管理。
> 更多信息：<https://keybase.io/docs/command_line>。

- 关注其他用户：

`keybase follow {{用户名}}`

- 添加新的证明：

`keybase prove {{服务}} {{服务用户名}}`

- 签署文件：

`keybase sign --infile {{输入文件}} --outfile {{输出文件}}`

- 验证签名文件：

`keybase verify --infile {{输入文件}} --outfile {{输出文件}}`

- 加密文件：

`keybase encrypt --infile {{输入文件}} --outfile {{输出文件}} {{接收者}}`

- 解密文件：

`keybase decrypt --infile {{输入文件}} --outfile {{输出文件}}`

- 撤销当前设备、注销并删除本地数据：

`keybase deprovision`