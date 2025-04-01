# rpmspec

> 查询 RPM spec 文件。
> 更多信息：<https://manned.org/rpmspec>.

- 列出由 RPM spec 文件生成的二进制包：

`rpmspec --query {{path/to/rpm.spec}}`

- 列出 `--queryformat` 的所有选项：

`rpmspec --querytags`

- 获取由 RPM spec 文件生成的单个二进制包的摘要信息：

`rpmspec --query --queryformat "{{%{name}: %{summary}\n}}" {{path/to/rpm.spec}}`

- 获取由 RPM spec 文件生成的源代码包：

`rpmspec --query --srpm {{path/to/rpm.spec}}`

- 解析 RPM spec 文件到 `stdout`：

`rpmspec --parse {{path/to/rpm.spec}}`