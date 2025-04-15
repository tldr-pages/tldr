# git cat-file

> 查看 Git 仓库对象的内容或类型和大小信息。
> 更多信息：<https://git-scm.com/docs/git-cat-file>.

- 获取 HEAD 提交的字节大小：

`git cat-file -s HEAD`

- 获取指定 Git 对象的类型（blob、tree、commit、tag）：

`git cat-file -t {{8c442dc3}}`

- 根据对象类型打印指定 Git 对象的内容：

`git cat-file -p {{HEAD~2}}`
