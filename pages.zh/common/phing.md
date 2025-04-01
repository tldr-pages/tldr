# phing

> 基于 Apache Ant 的 PHP 构建工具。
> 更多信息：<https://www.phing.info>.

- 执行 `build.xml` 文件中的默认任务：

`phing`

- 初始化一个新的构建文件：

`phing -i {{path/to/build.xml}}`

- 执行特定任务：

`phing {{task_name}}`

- 使用给定的构建文件路径：

`phing -f {{path/to/build.xml}} {{task_name}}`

- 将日志记录到指定文件：

`phing -logfile {{path/to/log_file}} {{task_name}}`

- 在构建中使用自定义属性：

`phing -D{{property}}={{value}} {{task_name}}`

- 指定自定义监听器类：

`phing -listener {{class_name}} {{task_name}}`

- 使用详细输出构建：

`phing -verbose {{task_name}}`
