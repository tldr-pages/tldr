# gitlint

> Git 提交信息检查器，用于检查提交信息的风格。
> 更多信息：<https://jorisroovers.com/gitlint/>.

- 检查最近的一次提交信息：

`gitlint`

- 要检查的提交范围：

`gitlint --commits {{single_refspec_argument}}`

- 包含额外用户定义规则的目录或 Python 模块路径：

`gitlint --extra-path {{path/to/directory}}`

- 启动特定的 CI 任务：

`gitlint --target {{path/to/target_directory}}`

- 包含 commit-msg 的文件路径：

`gitlint --msg-filename {{path/to/filename}}`

- 从本地存储库读取已暂存的提交元信息：

`gitlint --staged`