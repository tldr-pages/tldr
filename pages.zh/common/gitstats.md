# gitstats

> Git 仓库统计生成器。
> 更多信息：<https://gitstats.sourceforge.net>。

- 为本地仓库生成统计数据：

`gitstats {{path/to/git_repo/.git}} {{path/to/output_folder}}`

- 在 Windows（PowerShell）/ macOS / Linux 的网页浏览器中查看生成的统计数据：

`{{Invoke-Item|open|xdg-open}} {{path/to/output_folder/index.html}}`