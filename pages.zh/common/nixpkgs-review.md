# nixpkgs-review

> 用于审查 NixOS 软件包仓库（nixpkgs）中的拉取请求。
> 构建成功后，会启动包含所有已构建软件包的 `nix-shell` 环境。
> 更多信息： <https://github.com/Mic92/nixpkgs-review#usage>。

- 构建指定拉取请求中更改的软件包：

`nixpkgs-review pr {{pr_number|pr_url}}`

- 构建更改的软件包并发布带报告的评论（需在 `hub`、`gh` 或 `$GITHUB_TOKEN` 环境变量中配置令牌）：

`nixpkgs-review pr --post-result {{pr_number|pr_url}}`

- 构建更改的软件包并打印报告：

`nixpkgs-review pr --print-result {{pr_number|pr_url}}`

- 构建本地提交中更改的软件包：

`nixpkgs-review rev {{HEAD}}`

- 构建尚未提交的更改包：

`nixpkgs-review wip`

- 构建已暂存的更改包：

`nixpkgs-review wip --staged`
