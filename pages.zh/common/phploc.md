# phploc

> 快速测量 PHP 项目的大小并分析其结构。
> 更多信息：<https://github.com/sebastianbergmann/phploc>。

- 分析目录并打印结果：

`phploc {{path/to/directory}}`

- 仅包含列表中特定的文件（允许使用通配符）：

`phploc {{path/to/directory}} --names '{{path/to/file1,path/to/file2,...}}'`

- 从列表中排除特定的文件（允许使用通配符）：

`phploc {{path/to/directory}} --names-exclude '{{path/to/file1,path/to/file2,...}}'`

- 从分析中排除特定的目录：

`phploc {{path/to/directory}} --exclude {{path/to/exclude_directory}}`

- 将结果记录到特定的 CSV 文件中：

`phploc {{path/to/directory}} --log-csv {{path/to/file}}`

- 将结果记录到特定的 XML 文件中：

`phploc {{path/to/directory}} --log-xml {{path/to/file}}`

- 统计 PHPUnit 测试用例类和测试方法：

`phploc {{path/to/directory}} --count-tests`