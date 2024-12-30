# ansible-galaxy

> 执行各种与 Ansible 角色和集合相关的操作。
> 更多信息：<https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>。

- 列出已安装的角色或集合：

`ansible-galaxy {{role|collection}} list`

- 以不同的详细程度搜索角色（`-v` 应该在最后指定）：

`ansible-galaxy role search {{keyword}} -v{{vvvvv}}`

- 安装或移除角色：

`ansible-galaxy role {{install|remove}} {{role_name1 role_name2 ...}}`

- 创建一个新角色：

`ansible-galaxy role init {{role_name}}`

- 获取角色的信息：

`ansible-galaxy role info {{role_name}}`

- 安装或移除集合：

`ansible-galaxy collection {{install|remove}} {{collection_name1 collection_name2 ...}}`

- 显示关于角色或集合的帮助信息：

`ansible-galaxy {{role|collection}} {{-h|--help}}`