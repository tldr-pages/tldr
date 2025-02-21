# yq

> 一个轻量级且可移植的命令行 YAML 处理器。
> 更多信息：<https://mikefarah.gitbook.io/yq/>.

- 以漂亮打印格式输出 YAML 文件（v4+）：

`yq eval {{路径/到/file.yaml}}`

- 以漂亮打印格式输出 YAML 文件（v3）：

`yq read {{路径/到/file.yaml}} --colors`

- 输出仅包含数组的 YAML 文件中的第一个元素（v4+）：

`yq eval '.[0]' {{路径/到/file.yaml}}`

- 输出仅包含数组的 YAML 文件中的第一个元素（v3）：

`yq read {{路径/到/file.yaml}} '[0]'`

- 在文件中设置（或覆盖）键的值（v4+）：

`yq eval '.{{键}} = "{{值}}"' --inplace {{路径/到/file.yaml}}`

- 在文件中设置（或覆盖）键的值（v3）：

`yq write --inplace {{路径/到/file.yaml}} '{{键}}' '{{值}}'`

- 合并两个文件并打印到 `stdout`（v4+）：

`yq eval-all 'select(filename == "{{路径/到/file1.yaml}}") * select(filename == "{{路径/到/file2.yaml}}")' {{路径/到/file1.yaml}} {{路径/到/file2.yaml}}`

- 合并两个文件并打印到 `stdout`（v3）：

`yq merge {{路径/到/file1.yaml}} {{路径/到/file2.yaml}} --colors`
