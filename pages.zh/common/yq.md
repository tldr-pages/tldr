# yq

> 一个轻量级和可移植的命令行 YAML 处理器。
> 更多信息：<https://mikefarah.gitbook.io/yq/>。

- 以美观打印格式输出 YAML 文件 (v4+)：

`yq eval {{path/to/file.yaml}}`

- 以美观打印格式输出 YAML 文件 (v3)：

`yq read {{path/to/file.yaml}} --colors`

- 输出仅包含数组的 YAML 文件中的第一个元素 (v4+)：

`yq eval '.[0]' {{path/to/file.yaml}}`

- 输出仅包含数组的 YAML 文件中的第一个元素 (v3)：

`yq read {{path/to/file.yaml}} '[0]'`

- 在文件中设置（或覆盖）键的值 (v4+)：

`yq eval '.{{key}} = "{{value}}"' --inplace {{path/to/file.yaml}}`

- 在文件中设置（或覆盖）键的值 (v3)：

`yq write --inplace {{path/to/file.yaml}} '{{key}}' '{{value}}'`

- 合并两个文件并输出到 `stdout` (v4+)：

`yq eval-all 'select(filename == "{{path/to/file1.yaml}}") * select(filename == "{{path/to/file2.yaml}}")' {{path/to/file1.yaml}} {{path/to/file2.yaml}}`

- 合并两个文件并输出到 `stdout` (v3)：

`yq merge {{path/to/file1.yaml}} {{path/to/file2.yaml}} --colors`