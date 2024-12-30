# protector

> 保护或解除对 GitHub 仓库分支的保护。
> 更多信息：<https://github.com/jcgay/protector>。

- 保护 GitHub 仓库的分支（创建分支保护规则）：

`protector {{branches_regex}} -repos {{organization/repository}}`

- 使用干运行查看将会被保护的内容（也可以用于解除保护）：

`protector -dry-run {{branches_regex}} -repos {{organization/repository}}`

- 解除 GitHub 仓库的分支保护（删除分支保护规则）：

`protector -free {{branches_regex}} -repos {{organization/repository}}`