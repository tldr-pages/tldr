# molecule

> Molecule 有助于测试 Ansible 角色。
> 更多信息：<https://molecule.readthedocs.io>.

- 创建一个新的 Ansible 角色：

`molecule init role --role-name {{role_name}}`

- 运行测试：

`molecule test`

- 启动实例：

`molecule create`

- 配置实例：

`molecule converge`

- 列出实例的场景：

`molecule matrix converge`

- 登录实例：

`molecule login`