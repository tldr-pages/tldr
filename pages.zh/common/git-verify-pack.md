# git verify-pack

> 验证打包的 Git 存档文件。
> 更多信息：<https://git-scm.com/docs/git-verify-pack>。

- 验证一个打包的 Git 存档文件：

`git verify-pack {{path/to/pack-file}}`

- 验证一个打包的 Git 存档文件并显示详细信息：

`git verify-pack --verbose {{path/to/pack-file}}`

- 验证一个打包的 Git 存档文件并仅显示统计信息：

`git verify-pack --stat-only {{path/to/pack-file}}`