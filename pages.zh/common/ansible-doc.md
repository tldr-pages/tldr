# ansible-doc

> 显示已安装在 Ansible 库中的模块信息。
> 显示插件的简要列表及其简短描述。
> 更多信息：<https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>。

- 列出可用的操作插件（模块）：

`ansible-doc --list`

- 列出特定类型的可用插件：

`ansible-doc --type {{become|cache|callback|cliconf|connection|...}} --list`

- 显示特定操作插件（模块）的信息：

`ansible-doc {{plugin_name}}`

- 显示特定类型插件的信息：

`ansible-doc --type {{become|cache|callback|cliconf|connection|...}} {{plugin_name}}`

- 显示操作插件（模块）的 playbook 片段：

`ansible-doc --snippet {{plugin_name}}`

- 以 JSON 格式显示操作插件（模块）的信息：

`ansible-doc --json {{plugin_name}}`