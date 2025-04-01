# git filter-repo

> 一个多功能工具，用于重写 Git 历史。
> 另见：`bfg`。
> 更多信息：<https://github.com/newren/git-filter-repo>。

- 替换所有文件中的敏感字符串：

`git filter-repo --replace-text <(echo '{{find}}==>{{replacement}}')`

- 提取单个文件夹，保留历史记录：

`git filter-repo --path {{path/to/folder}}`

- 移除单个文件夹，保留历史记录：

`git filter-repo --path {{path/to/folder}} --invert-paths`

- 将子文件夹中的所有内容上移一级：

`git filter-repo --path-rename {{path/to/folder/:}}`