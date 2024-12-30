# pyinfra

> 大规模自动化基础设施。
> 更多信息请访问：<https://docs.pyinfra.com>。

- 通过 SSH 执行命令：

`pyinfra {{目标_IP_地址}} exec -- {{命令名称和参数}}`

- 在目标列表上执行部署文件的内容：

`pyinfra {{路径/到/目标列表.py}} {{路径/到/部署.py}}`

- 在本地执行命令：

`pyinfra @local {{路径/到/部署.py}}`

- 通过 Docker 执行命令：

`pyinfra @docker/{{容器}} {{路径/到/部署.py}}`