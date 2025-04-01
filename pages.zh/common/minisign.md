# minisign

> 一个极简的工具，用于签署文件和验证签名。
> 更多信息：<https://jedisct1.github.io/minisign/>.

- 在默认位置生成新的密钥对：

`minisign -G`

- 签署文件：

`minisign -Sm {{path/to/file}}`

- 签署文件，并在签名中添加一个可信（已签名）和一个不可信（未签名）的注释：

`minisign -Sm {{path/to/file}} -c "{{Untrusted comment}}" -t "{{Trusted comment}}"`

- 使用指定的公钥文件验证文件及其签名中的可信注释：

`minisign -Vm {{path/to/file}} -p {{path/to/publickey.pub}}`

- 指定一个Base64编码的公钥，验证文件及其签名中的可信注释：

`minisign -Vm {{path/to/file}} -P "{{public_key_base64}}"`
