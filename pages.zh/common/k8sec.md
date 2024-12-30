# k8sec

> 管理 Kubernetes 秘密。
> 更多信息：<https://github.com/dtan4/k8sec>。

- 列出所有秘密：

`k8sec list`

- 以 base64 编码字符串形式列出特定秘密：

`k8sec list {{secret_name}} --base64`

- 设置秘密的值：

`k8sec set {{secret_name}} {{key=value}}`

- 设置 base64 编码的值：

`k8sec set --base64 {{secret_name}} {{key=encoded_value}}`

- 取消设置秘密：

`k8sec unset {{secret_name}}`

- 从文件加载秘密：

`k8sec load -f {{path/to/file}} {{secret_name}}`

- 将秘密导出到文件：

`k8sec dump -f {{path/to/file}} {{secret_name}}`