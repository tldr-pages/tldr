# onefetch

> 显示本地 Git 仓库的项目信息和代码统计。
> 更多信息：<https://github.com/o2sh/onefetch/wiki/command-line-options>.

- 显示当前工作目录中 Git 仓库的统计信息：

`onefetch`

- 显示指定目录中 Git 仓库的统计信息：

`onefetch {{path/to/directory}}`

- 忽略由机器人提交的提交：

`onefetch --no-bots`

- 忽略合并提交：

`onefetch --no-merges`

- 不打印语言标志的 ASCII 艺术图：

`onefetch --no-art`

- 显示 `n` 个作者、语言或文件变更次数（默认：分别为 3、6 和 3）：

`onefetch --number-of-{{authors|languages|file-churns}} {{n}}`

- 忽略指定的文件和目录：

`onefetch {{[-e|--exclude]}} {{path/to/file_or_directory|regular_expression}}`

- 仅检测指定类别的语言（默认：编程和标记语言）：

`onefetch {{[-T|--type]}} {{programming|markup|prose|data}}`