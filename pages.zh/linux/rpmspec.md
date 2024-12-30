# rpmspec

> 查询 RPM 规格文件。
> 更多信息：<https://manned.org/rpmspec>。

- 列出从 RPM 规格文件生成的二进制包：

`rpmspec --query {{path/to/rpm.spec}}`

- 列出所有 `--queryformat` 的选项：

`rpmspec --querytags`

- 获取从 RPM 规格文件生成的单个二进制包的摘要信息：

`rpmspec --query --queryformat "{{%{name}: %{summary}\n}}" {{path/to/rpm.spec}}`

- 获取从 RPM 规格文件生成的源包：

`rpmspec --query --srpm {{path/to/rpm.spec}}`

- 解析 RPM 规格文件并输出到 `stdout`：

`rpmspec --parse {{path/to/rpm.spec}}`