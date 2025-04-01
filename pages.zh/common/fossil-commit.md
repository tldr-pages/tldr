# fossil commit

> 将文件提交到 Fossil 仓库。
> 更多信息：<https://fossil-scm.org/home/help/commit>。

- 创建一个包含当前签出版本中所有更改的新版本；用户将被提示输入注释：

`fossil commit`

- 创建一个包含当前签出版本中所有更改的新版本，并使用指定的注释：

`fossil commit --comment "{{comment}}"`

- 创建一个包含当前签出版本中所有更改的新版本，注释从指定文件中读取：

`fossil commit --message-file {{path/to/commit_message_file}}`

- 创建一个包含指定文件中更改的新版本；用户将被提示输入注释：

`fossil commit {{path/to/file1 path/to/file2 ...}}`