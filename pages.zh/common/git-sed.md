# git sed

> 使用 sed 替换 git 管理的文件中的模式。
> 这是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-sed>。

- 在当前仓库中替换指定文本：

`git sed '{{find_text}}' '{{replace_text}}'`

- 替换指定文本，并使用标准提交信息提交结果更改：

`git sed -c '{{find_text}}' '{{replace_text}}'`

- 使用正则表达式替换指定文本：

`git sed -f g '{{find_text}}' '{{replace_text}}'`

- 在给定目录下的所有文件中替换特定文本：

`git sed '{{find_text}}' '{{replace_text}}' -- {{path/to/directory}}`