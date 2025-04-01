# dvc gc

> 从缓存或远程存储中删除未使用的文件和目录。
> 更多信息：<https://dvc.org/doc/command-reference/gc>.

- 从缓存中清理垃圾，仅保留当前工作区引用的版本：

`dvc gc --workspace`

- 从缓存中清理垃圾，仅保留分支、标签和提交引用的版本：

`dvc gc --all-branches --all-tags --all-commits`

- 从缓存中清理垃圾，包括默认的云远程存储（如果已设置）：

`dvc gc --all-commits --cloud`

- 从缓存中清理垃圾，包括特定的云远程存储：

`dvc gc --all-commits --cloud --remote {{remote_name}}`