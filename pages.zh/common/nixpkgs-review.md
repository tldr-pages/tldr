# nixpkgs-review

> 审查 NixOS 软件包仓库 (nixpkgs) 中的拉取请求。
> 构建成功后，会启动包含所有已构建包的 `nix-shell`。
> 更多信息：<https://github.com/Mic92/nixpkgs-review#usage>。

- 构建指定拉取请求中更改的包：

`nixpkgs-review pr {{pr_number|pr_url}}`

- 构建更改的包并发布带有报告的评论（需要在 `hub`、`gh` 或 `GITHUB_TOKEN` 环境变量中设置令牌）：

`nixpkgs-review pr --post-result {{pr_number|pr_url}}`

- 构建更改的包并打印报告：

`nixpkgs-review pr --print-result {{pr_number|pr_url}}`

- 构建本地提交中更改的包：

`nixpkgs-review rev {{HEAD}}`

- 构建尚未提交的更改的包：

`nixpkgs-review wip`

- 构建已暂存的更改的包：

`nixpkgs-review wip --staged`