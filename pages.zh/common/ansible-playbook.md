# ansible-playbook

> 通过SSH协议在远程计算机上执行playbook中定义的任务.
> 主页: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- 执行playbook中的任务:

`ansible-playbook {{playbook}}`

- 在给定的主机清单文件中执行playbook中的命令:

`ansible-playbook {{playbook}} -i {{inventory_file}}`

- 通过定义在命令行中额外的变量执行playbook中的任务:

`ansible-playbook {{playbook}} -e "{{variable1}}={{value1}} {{variable2}}={{value2}}"`

- 通过定义在一个json格式的文件中额外的变量执行playbook中的任务:

`ansible-playbook {{playbook}} -e "@{{variables.json}}"`
