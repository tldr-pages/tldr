# ansible-lint

> 对你的自动化内容应用规则并遵循最佳实践。
> 更多信息：<https://docs.ansible.com/projects/lint/>.

- 对指定的 playbook 和角色目录进行静态检查：

`ansible-lint {{路径/到/playbook_文件}} {{路径/到/角色_目录}}`

- 在静态检查 playbook 时排除特定规则：

`ansible-lint {{[-x|--exclude-rules]}} {{规则1,规则2,...}} {{路径/到/playbook_文件}}`

- 以离线模式检查 playbook，并将输出格式化为 PEP8：

`ansible-lint {{[-o|--offline]}} {{[-p|--parseable]}} {{路径/到/playbook_文件}}`

- 使用自定义规则目录对 playbook 进行静态检查：

`ansible-lint {{[-r|--rules]}} {{路径/到/自定义_规则_目录}} {{路径/到/playbook_文件}}`

- 递归地检查指定目录中的所有 Ansible 内容：

`ansible-lint {{路径/到/项目_目录}}`
