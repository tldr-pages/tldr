# 许可

> 为开源项目创建许可文件。
> 更多信息：<https://nishanths.github.io/license>。

- 将许可打印到 `stdout`，使用默认设置（自动检测的作者名称和当前年份）：

`license {{license_name}}`

- 生成许可并保存到文件：

`license -o {{path/to/file}} {{license_name}}`

- 列出所有可用的许可：

`license ls`

- 生成具有自定义作者名称和年份的许可：

`license --name {{author}} --year {{release_year}} {{license_name}}`