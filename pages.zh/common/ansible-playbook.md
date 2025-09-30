# ansible-playbook

> 通过 SSH 协议在远程计算机上执行 playbook 中定义的任务。
> 更多信息：<https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- 执行 playbook 中的任务：

`ansible-playbook {{playbook}}`

- 使用自定义主机清单执行 playbook 中的任务：

`ansible-playbook {{playbook}} {{[-i|--inventory]}} {{清单文件}}`

- 使用通过命令行定义的额外变量执行 playbook 中的任务：

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "{{变量1}}={{值1}} {{变量2}}={{值2}}"`

- 使用在 JSON 文件中定义的额外变量执行 playbook 中的任务：

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "@{{变量.json}}"`

- 执行 playbook 中的指定标签的任务：

`ansible-playbook {{playbook}} {{[-t|--tags|]}} {{标签1,标签2}}`

- 从指定任务开始执行 playbook 中的任务：

`ansible-playbook {{playbook}} --start-at {{任务名称}}`

- 以不做任何更改（试执行）方式执行 playbook 中的任务：

`ansible-playbook {{playbook}} {{[-C|--check|]}} {{[-D|--diff|]}}`
