# scoop bucket

> Manage buckets: Git repositories containing files which describe how scoop installs applications.
> If Scoop doesn't know where the bucket is located its repository location must be specified.
> 更多信息: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- 列出所有正在使用的 bucket:

`scoop bucket list`

- 列出所有已知 bucket:

`scoop bucket known`

- 按名称添加一个已知 bucket:

`scoop bucket add {{名称}}`

- 通过名称和 Git 存储库 URL 添加未知 bucket:

`scoop bucket add {{名称}} {{https://example.com/repository.git}}`

- 按名称删除 bucket:

`scoop bucket rm {{名称}}`
