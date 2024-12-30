# bat

> 打印并连接文件。
> 一个具有语法高亮和 Git 集成的 `cat` 克隆。
> 更多信息：<https://github.com/sharkdp/bat>。

- 将一个或多个文件的内容美观地打印到 `stdout`：

`bat {{path/to/file1 path/to/file2 ...}}`

- 将多个文件连接到目标文件中：

`bat {{path/to/file1 path/to/file2 ...}} > {{path/to/target_file}}`

- 移除装饰并禁用分页（`--style plain` 可以用 `-p` 替代，或者两个选项都用 `-pp`）：

`bat --style plain --pager never {{path/to/file}}`

- 用不同的背景色高亮显示特定行或行范围：

`bat {{-H|--highlight-line}} {{10|5:10|:10|10:|10:+5}} {{path/to/file}}`

- 显示不可打印字符，如空格、制表符或换行符：

`bat {{-A|--show-all}} {{path/to/file}}`

- 在输出中移除所有装饰，保留行号：

`bat {{-n|--number}} {{path/to/file}}`

- 通过显式设置语言为 JSON 文件提供语法高亮：

`bat {{-l|--language}} json {{path/to/file.json}}`

- 显示所有支持的语言：

`bat {{-L|--list-languages}}`