# patool

> 归档文件管理器。
> 支持创建、提取、测试、列出、搜索、重新打包和比较各种归档格式。
> 更多信息：<https://github.com/wummel/patool>。

- 提取归档文件：

`patool extract {{path/to/archive}}`

- 列出归档文件的内容：

`patool list {{path/to/archive}}`

- 比较两个归档文件的内容，并在标准输出中显示差异：

`patool diff {{path/to/archive1}} {{path/to/archive2}}`

- 在归档文件的内容中搜索字符串：

`patool search {{path/to/archive}}`