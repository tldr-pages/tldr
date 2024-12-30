# minisign

> 一个非常简单的工具，用于签署文件和验证签名。
> 更多信息：<https://jedisct1.github.io/minisign/>.

- 在默认位置生成一个新的密钥对：

`minisign -G`

- 签署一个文件：

`minisign -Sm {{path/to/file}}`

- 签署一个文件，在签名中添加一个可信（已签名）和一个不可信（未签名）评论：

`minisign -Sm {{path/to/file}} -c "{{Untrusted comment}}" -t "{{Trusted comment}}"`

- 使用指定的公钥文件验证一个文件及其签名中的可信评论：

`minisign -Vm {{path/to/file}} -p {{path/to/publickey.pub}}`

- 验证一个文件及其签名中的可信评论，指定一个作为 Base64 编码的公钥：

`minisign -Vm {{path/to/file}} -P "{{public_key_base64}}"`