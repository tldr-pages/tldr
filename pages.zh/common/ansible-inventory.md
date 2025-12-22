# ansible-inventory

> 显示或转储 Ansible 清单。
> 请参阅：`ansible`
> 更多信息：<https://docs.ansible.com/projects/ansible/latest/cli/ansible-inventory.html>.

- 显示默认清单：

`ansible-inventory --list`

- 显示自定义清单：

`ansible-inventory --list {{[-i|--inventory-file]}} {{路径/到/文件_或_脚本_或_目录}}`

- 以 YAML 格式显示默认清单：

`ansible-inventory --list {{[-y|--yaml]}}`

- 将默认清单转储到文件：

`ansible-inventory --list --output {{路径/到/文件}}`
