# bfg

> 像 git-filter-branch 一样，从 Git 历史中移除大文件或密码。
> 注意：如果您的仓库连接到远程，您需要强制推送到远程。
> 更多信息请访问：<https://rtyley.github.io/bfg-repo-cleaner/>.

- 移除包含敏感数据的文件，但保留最新提交不变：

`bfg --delete-files {{file_with_sensitive_data}}`

- 移除在指定文件中提到的所有文本，无论其在仓库历史中的何处出现：

`bfg --replace-text {{path/to/file.txt}}`