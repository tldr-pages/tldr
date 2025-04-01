# dvc diff

> 显示 DVC 跟踪的文件和目录的变化。
> 更多信息：<https://dvc.org/doc/command-reference/diff>.

- 比较不同 Git 提交、标签和分支与当前工作区的 DVC 跟踪文件：

`dvc diff {{commit_hash/tag/branch}}`

- 比较两个 Git 提交之间的 DVC 跟踪文件的变化：

`dvc diff {{revision1}} {{revision2}}`

- 比较 DVC 跟踪文件及其最新的哈希值：

`dvc diff --show-hash {{commit}}`

- 比较 DVC 跟踪文件，并以 JSON 格式显示输出：

`dvc diff --show-json --show-hash {{commit}}`

- 比较 DVC 跟踪文件，并以 Markdown 格式显示输出：

`dvc diff --show-md --show-hash {{commit}}`