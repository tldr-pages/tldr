# git write-tree

> 低级实用工具，用于从当前索引创建树对象。
> 更多信息：<https://git-scm.com/docs/git-write-tree>。

- 从当前索引创建树对象：

`git write-tree`

- 创建一个树对象，而不检查目录中引用的对象是否存在于对象数据库中：

`git write-tree --missing-ok`

- 创建一个表示子目录的树对象（用于为指定子目录中的子项目写入树对象）：

`git write-tree --prefix {{subdirectory}}/`