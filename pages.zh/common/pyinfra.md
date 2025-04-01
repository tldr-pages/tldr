# pyinfra

> 自动化大规模的基础设施。
> 更多信息：<https://docs.pyinfra.com>。

- 通过 SSH 执行命令：

`pyinfra {{target_ip_address}} exec -- {{command_name_and_arguments}}`

- 在目标列表上执行部署文件的内容：

`pyinfra {{path/to/target_list.py}} {{path/to/deploy.py}}`

- 在本地执行命令：

`pyinfra @local {{path/to/deploy.py}}`

- 通过 Docker 执行命令：

`pyinfra @docker/{{container}} {{path/to/deploy.py}}`