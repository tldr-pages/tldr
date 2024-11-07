# ansible-playbook

> 通过 SSH 协议在远程计算机上执行 playbook 中定义的任务。
> 更多信息：<https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- 执行 playbook 中的任务：

`ansible-playbook {{playbook}}`

- 使用自定义主机清单执行 playbook 中的任务：

`ansible-playbook {{playbook}} -i {{inventory_file}}`

- 使用通过命令行定义的额外变量执行 playbook 中的任务：

`ansible-playbook {{playbook}} -e "{{variable1}}={{value1}} {{variable2}}={{value2}}"`

- 使用在 JSON 文件中定义的额外变量执行 playbook 中的任务：

`ansible-playbook {{playbook}} -e "@{{variables.json}}"`

- 执行 playbook 中的指定标签的任务：

`ansible-playbook {{playbook}} --tags {{tag1,tag2}}`

- 从指定任务开始执行 playbook 中的任务：

`ansible-playbook {{playbook}} --start-at {{task_name}}`

- 以不做任何更改（试执行）方式执行 playbook 中的任务：

`ansible-playbook {{playbook}} --check --diff`
