# bfg

> 从 Git 历史记录中删除大文件或密码，类似于 git-filter-branch。
> 注意：如果您的仓库连接到了远程仓库，您需要强制推送更改。
> 更多信息：<https://rtyley.github.io/bfg-repo-cleaner/>.

- 删除包含敏感数据的文件，但保留最新的提交：

`bfg --delete-files {{file_with_sensitive_data}}`

- 从仓库的历史记录中删除指定文件中提到的所有文本：

`bfg --replace-text {{path/to/file.txt}}`