# hut

> 一个用于 sourcehut 的 CLI 工具。
> 更多信息：<https://manned.org/hut>。

- 初始化 `hut` 的配置文件（这将提示输入 OAuth2 访问令牌，这是使用 `hut` 所必需的）：

`hut init`

- 列出 Git/Mercurial 仓库：

`hut {{git|hg}} list`

- 创建一个公共 Git/Mercurial 仓库：

`hut {{git|hg}} create {{name}}`

- 列出 <https://builds.sr.ht> 上的作业：

`hut builds list`

- 显示作业的状态：

`hut builds show {{job_id}}`

- SSH 进入作业容器：

`hut ssh {{job_id}}`