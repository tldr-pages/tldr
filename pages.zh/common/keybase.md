# keybase

> 用于将社交媒体身份映射到加密密钥的公共可审计目录。
> 更多信息：<https://keybase.io/docs/command_line>.

- 关注其他用户：

`keybase follow {{username}}`

- 添加新的证明：

`keybase prove {{service}} {{service_username}}`

- 签名文件：

`keybase sign --infile {{input_file}} --outfile {{output_file}}`

- 验证签名文件：

`keybase verify --infile {{input_file}} --outfile {{output_file}}`

- 加密文件：

`keybase encrypt --infile {{input_file}} --outfile {{output_file}} {{receiver}}`

- 解密文件：

`keybase decrypt --infile {{input_file}} --outfile {{output_file}}`

- 注销当前设备，删除本地数据：

`keybase deprovision`