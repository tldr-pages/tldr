# hub fork

> 叉一个 GitHub 仓库。类似于 `git-extras` 中的 `git fork`。
> 更多信息：<https://hub.github.com/hub-fork.1.html>.

- 通过仓库的 slug 叉一个 GitHub 仓库：

`hub fork {{tldr-pages/tldr}}`

- 通过仓库的 URL 叉一个 GitHub 仓库：

`hub fork {{https://github.com/tldr-pages/tldr}}`

- 叉当前的 GitHub 仓库，并将远端名称设置为 origin：

`hub fork --remote-name {{origin}}`