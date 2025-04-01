# copr-cli

> 与 Fedora-Projects 的 copr 实例交互，用于构建 RPMs 和发布它们。
> 更多信息：<https://manned.org/copr-cli>.

- 显示登录到 copr 的用户：

`copr-cli whoami`

- 在 copr 上构建本地 spec 文件：

`copr-cli build {{repository}} {{path/to/spec_file}}`

- 查看构建状态：

`copr-cli list-builds {{repository}}`

- 触发从公共（git）仓库构建 spec 文件的 copr 构建：

`copr-cli buildscm {{repository}} --clone-url {{https://git.example.org/repo}} --spec {{spec_file_name}}`
