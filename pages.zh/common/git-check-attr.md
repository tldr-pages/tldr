# git check-attr

> 对于每个路径名，列出该路径名上每个属性是否未指定、已设置或未设置。
> 更多信息：<https://git-scm.com/docs/git-check-attr>.

- 检查文件上所有属性的值：

`git check-attr --all {{path/to/file}}`

- 检查文件上特定属性的值：

`git check-attr {{attribute}} {{path/to/file}}`

- 检查特定文件上所有属性的值：

`git check-attr --all {{path/to/file1 path/to/file2 ...}}`

- 检查一个或多个文件上特定属性的值：

`git check-attr {{attribute}} {{path/to/file1 path/to/file2 ...}}`
