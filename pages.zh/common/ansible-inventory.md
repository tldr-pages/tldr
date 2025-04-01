# ansible-inventory

> 显示或导出 Ansible 库存。
> 另请参阅：`ansible`。
> 更多信息：<https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>。

- 显示默认库存：

`ansible-inventory --list`

- 显示自定义库存：

`ansible-inventory --list --inventory {{path/to/file_or_script_or_directory}}`

- 以 YAML 格式显示默认库存：

`ansible-inventory --list --yaml`

- 将默认库存导出到文件：

`ansible-inventory --list --output {{path/to/file}}`
