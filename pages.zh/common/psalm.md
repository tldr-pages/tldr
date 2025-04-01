# psalm

> 一个用于查找 PHP 应用中错误的静态分析工具。
> 更多信息：<https://psalm.dev>。

- 生成一个 Psalm 配置文件：

`psalm --init`

- 分析当前工作目录：

`psalm`

- 分析特定目录或文件：

`psalm {{path/to/file_or_directory}}`

- 使用特定配置文件分析项目：

`psalm --config {{path/to/psalm.xml}}`

- 在输出中包含信息性发现：

`psalm --show-info`

- 分析项目并显示统计信息：

`psalm --stats`

- 使用 4 个线程并行分析项目：

`psalm --threads {{4}}`
