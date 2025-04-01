# license

> 为开源项目创建许可文件。
> 更多信息：<https://nishanths.github.io/license>.

- 使用默认值（自动检测的作者姓名，和当前年份）将许可打印到 `stdout`：

`license {{license_name}}`

- 生成许可证并将其保存到文件中：

`license -o {{path/to/file}} {{license_name}}`

- 列出所有可用的许可证：

`license ls`

- 生成带有自定义作者姓名和年份的许可：

`license --name {{author}} --year {{release_year}} {{license_name}}`
