# git difftool

> 使用外部差异工具显示文件更改。接受与 `git diff` 相同的选项和参数。
> 参见：`git diff`。
> 更多信息：<https://git-scm.com/docs/git-difftool>。

- 列出可用的差异工具：

`git difftool --tool-help`

- 将默认差异工具设置为 meld：

`git config --global diff.tool "{{meld}}"`

- 使用默认的差异工具显示暂存的更改：

`git difftool --staged`

- 使用指定的工具 (opendiff) 显示从某次提交以来的更改：

`git difftool --tool={{opendiff}} {{commit}}`