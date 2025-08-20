# git check-ignore

> 分析和调试 Git 忽略规则（.gitignore 文件）。
> 更多信息：<https://git-scm.com/docs/git-check-ignore>.

- 检查文件或目录是否被忽略：

`git check-ignore {{路径/到/文件或目录}}`

- 检查多个文件或目录是否被忽略：

`git check-ignore {{路径/到/文件或目录1 路径/到/文件或目录2 ...}}`

- 从标准输入读取路径列表（每行一个路径）：

`git check-ignore --stdin < {{路径/到/文件列表}}`

- 不检查索引（用于调试为何某些路径被跟踪而非忽略）：

`git check-ignore --no-index {{路径/到/文件或目录1 路径/到/文件或目录2 ...}}`

- 显示每个路径匹配的具体忽略规则：

`git check-ignore {{[-v|--verbose]}} {{路径/到/文件或目录1 路径/到/文件或目录2 ...}}`
