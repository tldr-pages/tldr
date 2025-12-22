# ansible-doc

> 显示 Ansible 库中已安装模块的信息。
> 显示插件及其简短描述的精简列表。
> 更多信息：<https://docs.ansible.com/projects/ansible/latest/cli/ansible-doc.html>.

- 列出可用的动作插件（模块）：

`ansible-doc {{[-l|--list]}}`

- 列出指定类型的可用插件：

`ansible-doc {{[-t|--type]}} {{become|cache|callback|cliconf|connection|...}} {{[-l|--list]}}`

- 显示指定动作插件（模块）的信息：

`ansible-doc {{plugin_name}}`

- 显示指定类型插件的信息：

`ansible-doc {{[-t|--type]}} {{become|cache|callback|cliconf|connection|...}} {{plugin_name}}`

- 显示动作插件（模块）的 playbook 代码片段：

`ansible-doc {{[-s|--snippet]}} {{plugin_name}}`

- 以 JSON 格式显示动作插件（模块）的信息：

`ansible-doc {{[-j|--json]}} {{plugin_name}}`
