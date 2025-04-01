# k8sec

> 管理 Kubernetes 密钥。
> 更多信息：<https://github.com/dtan4/k8sec>.

- 列出所有密钥：

`k8sec list`

- 以 base64 编码字符串的形式列出特定密钥：

`k8sec list {{secret_name}} --base64`

- 设置密钥的值：

`k8sec set {{secret_name}} {{key=value}}`

- 设置 base64 编码的值：

`k8sec set --base64 {{secret_name}} {{key=encoded_value}}`

- 删除密钥：

`k8sec unset {{secret_name}}`

- 从文件加载密钥：

`k8sec load -f {{path/to/file}} {{secret_name}}`

- 将密钥导出到文件：

`k8sec dump -f {{path/to/file}} {{secret_name}}`