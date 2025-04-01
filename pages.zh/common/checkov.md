# checkov

> Checkov 是一个用于基础架构即代码 (IaC) 的静态代码分析工具。
> 它也是一个用于镜像和开源包的软件组成分析 (SCA) 工具。
> 更多信息：<https://www.checkov.io/1.Welcome/Quick%20Start.html>。

- 扫描包含 IaC（Terraform、Cloudformation、ARM、Ansible、Bicep、Dockerfile 等）的目录：

`checkov --directory {{path/to/directory}}`

- 扫描 IaC 文件，输出中省略代码块：

`checkov --compact --file {{path/to/file}}`

- 列出所有 IaC 类型的所有检查项：

`checkov --list`