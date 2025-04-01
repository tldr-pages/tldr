# git fsck

> 验证 Git 仓库索引中节点的有效性和连通性。
> 不会进行任何修改。
> 参见：`git gc` 用于清理悬挂的 blob。
> 更多信息：<https://git-scm.com/docs/git-fsck>。

- 检查当前仓库：

`git fsck`

- 列出所有找到的标签：

`git fsck --tags`

- 列出所有找到的根节点：

`git fsck --root`