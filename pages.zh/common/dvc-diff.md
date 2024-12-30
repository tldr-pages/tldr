# dvc diff

> 显示 DVC 跟踪的文件和目录的变化。
> 更多信息：<https://dvc.org/doc/command-reference/diff>。

- 比较当前工作区与不同 Git 提交、标签和分支的 DVC 跟踪文件：

`dvc diff {{commit_hash/tag/branch}}`

- 比较从一个 Git 提交到另一个 Git 提交的 DVC 跟踪文件的变化：

`dvc diff {{revision1}} {{revision2}}`

- 比较 DVC 跟踪文件及其最新哈希：

`dvc diff --show-hash {{commit}}`

- 比较 DVC 跟踪文件，输出以 JSON 格式显示：

`dvc diff --show-json --show-hash {{commit}}`

- 比较 DVC 跟踪文件，输出以 Markdown 格式显示：

`dvc diff --show-md --show-hash {{commit}}`