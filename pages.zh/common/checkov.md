# checkov

> Checkov 是一个用于基础设施即代码（IaC）的静态代码分析工具。
> 它也是一个用于图像和开源包的软件组成分析（SCA）工具。
> 更多信息请访问：<https://www.checkov.io/1.Welcome/Quick%20Start.html>。

- 扫描包含 IaC 的目录（Terraform、Cloudformation、ARM、Ansible、Bicep、Dockerfile 等）：

`checkov --directory {{path/to/directory}}`

- 扫描一个 IaC 文件，输出中省略代码块：

`checkov --compact --file {{path/to/file}}`

- 列出所有 IaC 类型的所有检查：

`checkov --list`