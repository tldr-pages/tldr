# scoop bucket

> 管理 bucket: 包含描述 scoop 应如何安装应用程序的文件的 Git 存储库。
> 如果 Scoop 不知道 bucket 在哪里，则必须指定其存储库位置。
> 更多信息：<https://github.com/lukesampson/scoop/wiki/Buckets>.

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
