# git fame

> 美观地打印 Git 仓库贡献。
> 更多信息：<https://github.com/casperdcl/git-fame>。

- 计算当前 Git 仓库的贡献：

`git fame`

- 排除与指定正则表达式匹配的文件/目录：

`git fame --excl "{{正则表达式}}"`

- 计算在指定日期之后的贡献：

`git fame --since "{{3周前|2021-05-13}}"`

- 以指定格式显示贡献：

`git fame --format {{管道|yaml|json|csv|tsv}}`

- 按文件扩展名显示贡献：

`git fame --bytype`

- 忽略空格变更：

`git fame --ignore-whitespace`

- 检测文件间的行移动和复制：

`git fame -C`

- 检测文件内的行移动和复制：

`git fame -M`