# ansible-playbook

> 在远程机器上通过 SSH 执行 playbook 中定义的任务。
> 更多信息：<https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>。

- 运行 playbook 中的任务：

`ansible-playbook {{playbook}}`

- 使用自定义主机 [i]nventory 运行 playbook 中的任务：

`ansible-playbook {{playbook}} -i {{inventory_file}}`

- 使用命令行定义的 [e]xtra 变量运行 playbook 中的任务：

`ansible-playbook {{playbook}} -e "{{variable1}}={{value1}} {{variable2}}={{value2}}"`

- 使用 JSON 文件中定义的 [e]xtra 变量运行 playbook 中的任务：

`ansible-playbook {{playbook}} -e "@{{variables.json}}"`

- 针对给定标签运行 playbook 中的任务：

`ansible-playbook {{playbook}} --tags {{tag1,tag2}}`

- 从特定任务开始运行 playbook 中的任务：

`ansible-playbook {{playbook}} --start-at {{task_name}}`

- 在不做任何更改的情况下运行 playbook 中的任务（干运行）：

`ansible-playbook {{playbook}} --check --diff`