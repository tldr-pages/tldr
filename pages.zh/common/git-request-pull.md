# git request-pull

> 生成一个请求，要求上游项目将更改合并到其项目中。
> 更多信息：<https://git-scm.com/docs/git-request-pull>.

- 生成一个请求，概述从 v1.1 版本到指定分支之间的更改：

`git request-pull {{v1.1}} {{https://example.com/project}} {{branch_name}}`

- 生成一个请求，概述从 `foo` 分支的 v0.1 版本到本地 `bar` 分支之间的更改：

`git request-pull {{v0.1}} {{https://example.com/project}} {{foo:bar}}`