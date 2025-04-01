# uncrustify

> C、C++、C#、D、Java 和 Pawn 源代码格式化工具。
> 更多信息：<https://github.com/uncrustify/uncrustify>.

- 格式化单个文件：

`uncrustify -f {{路径/到/文件.cpp}} -o {{路径/到/输出文件.cpp}}`

- 从 `stdin` 读取文件名，在写回原始文件路径之前创建备份：

`find . -name "*.cpp" | uncrustify -F - --replace`

- 不进行备份（适用于文件已在版本控制下的情况）：

`find . -name "*.cpp" | uncrustify -F - --no-backup`

- 使用自定义配置文件并将结果写入 `stdout`：

`uncrustify -c {{路径/到/uncrustify.cfg}} -f {{路径/到/文件.cpp}}`

- 显式设置配置变量的值：

`uncrustify --set {{选项}}={{值}}`

- 生成新的配置文件：

`uncrustify --update-config -o {{路径/到/新配置文件.cfg}}`
