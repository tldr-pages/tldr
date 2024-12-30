# gitlint

> Git 提交消息检查器检查您的提交消息的格式。
> 更多信息：<https://jorisroovers.com/gitlint/>.

- 检查最后一次提交消息：

`gitlint`

- 要检查的提交范围：

`gitlint --commits {{single_refspec_argument}}`

- 包含额外用户定义规则的目录或 Python 模块的路径：

`gitlint --extra-path {{path/to/directory}}`

- 启动特定的 CI 作业：

`gitlint --target {{path/to/target_directory}}`

- 包含提交消息的文件路径：

`gitlint --msg-filename {{path/to/filename}}`

- 从本地仓库读取暂存的提交元信息：

`gitlint --staged`