# git check-attr

> 检查每个路径的文件属性状态（未指定/已设置/未设置）。
> 更多信息：<https://git-scm.com/docs/git-check-attr>.

- 检查文件的所有属性状态：

`git check-attr --all {{路径/到/文件}}`

- Check the value of a specific attribute on a file:

`git check-attr {{属性}} {{路径/到/文件}}`

- Check the values of all attributes on specific files:

`git check-attr --all {{路径/到/文件1 路径/到/文件2 ...}}`

- Check the value of a specific attribute on one or more files:

`git check-attr {{属性}} {{路径/到/文件1 路径/到/文件2 ...}}`
