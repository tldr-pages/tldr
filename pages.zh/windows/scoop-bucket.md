# 软碗

> 管理软碗：包含描述 Scoop 如何安装应用程序的文件的 Git 仓库。
> 如果 Scoop 不知道软碗的位置，则必须指定其仓库位置。
> 更多信息：<https://github.com/lukesampson/scoop/wiki/Buckets>。

- 列出当前正在使用的所有软碗：

`scoop bucket list`

- 列出所有已知的软碗：

`scoop bucket known`

- 通过名称添加已知的软碗：

`scoop bucket add {{name}}`

- 通过名称和 Git 仓库 URL 添加未知的软碗：

`scoop bucket add {{name}} {{https://example.com/repository.git}}`

- 通过名称删除软碗：

`scoop bucket rm {{name}}`