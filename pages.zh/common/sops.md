# sops

> SOPS（Secrets OPerationS）：一个简单且灵活的管理密钥的工具。
> 更多信息：<https://github.com/mozilla/sops>.

- 加密文件：

`sops -e {{path/to/file.json}} > {{path/to/file.enc.json}}`

- 解密文件到 `stdout`：

`sops -d {{path/to/file.enc.json}}`

- 更新 `sops` 文件中声明的密钥：

`sops updatekeys {{path/to/file.enc.yaml}}`

- 旋转 `sops` 文件的数据密钥：

`sops -r {{path/to/file.enc.yaml}}`

- 文件加密后更改其扩展名：

`sops -d --input-type json {{path/to/file.enc.json}}`

- 通过命名密钥和通过编号索引数组元素来提取它们：

`sops -d --extract '["an_array"][1]' {{path/to/file.enc.json}}`

- 显示两个 `sops` 文件之间的差异：

`diff <(sops -d {{path/to/secret1.enc.yaml}}) <(sops -d {{path/to/secret2.enc.yaml}})`