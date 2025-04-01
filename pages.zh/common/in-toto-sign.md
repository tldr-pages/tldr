# in-toto-sign

> 签署或验证 in-toto 链接或布局元数据。
> 更多信息：<https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-sign.html>.

- 使用两个密钥签署 'unsigned.layout' 并将其写入 'root.layout'：

`in-toto-sign -f {{unsigned.layout}} -k {{priv_key1}} {{priv_key2}} -o {{root.layout}}`

- 替换链接文件中的签名并写入默认文件名：

`in-toto-sign -f {{package.2f89b927.link}} -k {{priv_key}}`

- 验证使用 3 个密钥签署的布局：

`in-toto-sign -f {{root.layout}} -k {{pub_key0}} {{pub_key1}} {{pub_key2}} --verify`

- 使用默认 GPG 密钥环中的默认 GPG 密钥签署布局：

`in-toto-sign -f {{root.layout}} --gpg`

- 使用 keyid 为 '...439F3C2' 的 GPG 密钥验证布局：

`in-toto-sign -f {{root.layout}} --verify --gpg {{...439F3C2}}`