# ostree

> 类似于 `git` 的二进制文件版本控制，但针对操作系统根文件系统进行了优化。
> OSTree 是像 Fedora Silverblue、Fedora IoT 或 Fedora CoreOS 这样的不可变镜像基础操作系统的基础。
> 更多信息：<https://ostreedev.github.io/ostree>。

- 使用 `$PWD` 中的文件初始化一个包含元数据的仓库，元数据存储在 `$PWD/path/to/repo` 中：

`ostree init --repo {{path/to/repo}}`

- 创建文件的提交（快照）：

`ostree commit --repo {{path/to/repo}} --branch {{branch_name}}`

- 显示提交中的文件：

`ostree ls --repo {{path/to/repo}} {{commit_id}}`

- 显示提交的元数据：

`ostree show --repo {{path/to/repo}} {{commit_id}}`

- 显示提交列表：

`ostree log --repo {{path/to/repo}} {{branch_name}}`

- 显示仓库摘要：

`ostree summary --repo {{path/to/repo}} --view`

- 显示可用的引用（分支）：

`ostree refs --repo {{path/to/repo}}`