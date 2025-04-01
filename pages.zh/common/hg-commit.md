# hg commit

> 将所有已暂存或指定的文件提交到仓库。
> 更多信息：<https://www.mercurial-scm.org/doc/hg.1.html#commit>.

- 将已暂存的文件提交到仓库：

`hg commit`

- 提交特定文件或目录：

`hg commit {{path/to/file_or_directory}}`

- 带有特定提交信息的提交：

`hg commit --message {{message}}`

- 提交所有匹配指定模式的文件：

`hg commit --include {{pattern}}`

- 提交所有文件，但排除匹配指定模式的文件：

`hg commit --exclude {{pattern}}`

- 使用交互模式提交：

`hg commit --interactive`