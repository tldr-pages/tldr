# git filter-repo

> 一个用于重写 Git 历史的多功能工具。
> 另见：`bfg`。
> 更多信息：<https://github.com/newren/git-filter-repo>。

- 在所有文件中替换敏感字符串：

`git filter-repo --replace-text <(echo '{{find}}==>{{replacement}}')`

- 提取一个文件夹，保留历史：

`git filter-repo --path {{path/to/folder}}`

- 移除一个文件夹，保留历史：

`git filter-repo --path {{path/to/folder}} --invert-paths`

- 将子文件夹中的所有内容上移一级：

`git filter-repo --path-rename {{path/to/folder/:}}`