# ansible-playbook

> 通过 SSH 协议在远程计算机上执行 playbook 中定义的任务。
> 更多信息：<https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- 执行 playbook 中的任务：

`ansible-playbook {{playbook}}`

- 在给定的主机清单文件中执行 playbook 中的命令：

`ansible-playbook {{playbook}} -i {{清单文件}}`

- 通过定义在命令行中额外的变量执行 playbook 中的任务：

`ansible-playbook {{playbook}} -e "{{变量 1}}={{值 1}} {{变量 2}}={{值 2}}"`

- 通过定义在一个 json 格式的文件中额外的变量执行 playbook 中的任务：

`ansible-playbook {{playbook}} -e "@{{variables.json}}"`
