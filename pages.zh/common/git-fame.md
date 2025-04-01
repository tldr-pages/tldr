# git fame

> 以美观的格式显示 Git 仓库的贡献。
> 更多信息：<https://github.com/casperdcl/git-fame>.

- 计算当前 Git 仓库的贡献：

`git fame`

- 排除符合指定正则表达式的文件/目录：

`git fame --excl "{{regular_expression}}"`

- 计算指定日期后的贡献：

`git fame --since "{{3 weeks ago|2021-05-13}}"`

- 以指定格式显示贡献：

`git fame --format {{pipe|yaml|json|csv|tsv}}`

- 按文件扩展名显示贡献：

`git fame --bytype`

- 忽略空白字符的变化：

`git fame --ignore-whitespace`

- 检测文件间行的移动和复制：

`git fame -C`

- 检测文件内行的移动和复制：

`git fame -M`
