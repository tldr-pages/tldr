# cargo 安装

> 构建并安装一个 Rust 二进制文件。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-install.html>。

- 从 <https://crates.io> 安装一个包（版本是可选的 - 默认使用最新版本）：

`cargo install {{package}}@{{version}}`

- 从指定的 Git 仓库安装一个包：

`cargo install --git {{repo_url}}`

- 从 Git 仓库安装时，构建指定的分支/标签/提交：

`cargo install --git {{repo_url}} --{{branch|tag|rev}} {{branch_name|tag|commit_hash}}`

- 列出所有已安装的包及其版本：

`cargo install --list`