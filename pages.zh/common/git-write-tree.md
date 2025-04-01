# git write-tree

> 从当前索引创建树对象的底层工具。
> 更多信息：<https://git-scm.com/docs/git-write-tree>。

- 从当前索引创建一个树对象：

`git write-tree`

- 创建一个树对象，不检查目录引用的对象是否存在于对象数据库中：

`git write-tree --missing-ok`

- 创建一个表示子目录的树对象（用于为命名子目录中的子项目写入树对象）：

`git write-tree --prefix {{subdirectory}}/`
