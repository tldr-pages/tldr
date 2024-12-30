# git request-pull

> 生成请求，要求上游项目将更改合并到其树中。
> 更多信息：<https://git-scm.com/docs/git-request-pull>。

- 生成请求，概述 v1.1 发布与指定分支之间的更改：

`git request-pull {{v1.1}} {{https://example.com/project}} {{branch_name}}`

- 生成请求，概述 v0.1 发布在 `foo` 分支与本地 `bar` 分支之间的更改：

`git request-pull {{v0.1}} {{https://example.com/project}} {{foo:bar}}`