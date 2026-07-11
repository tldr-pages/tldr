# test

> 检查文件类型，比较数值。
> 如果条件评估为真，则返回 0，如果评估为假，则返回 1。
> 另请参阅：`[`。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/test-invocation.html>。

- 测试指定的变量是否等于指定的字符串：

`test "{{$MY_VAR}}" = "{{/bin/zsh}}"`

- 测试指定的变量是否为空（[z]ero 长度）：

`test -z "{{$GIT_BRANCH}}"`

- 测试指定的文件是否存在（[f]ile）：

`test -f "{{路径/到/文件}}"`

- 测试指定的目录是否不存在（[d]irectory）：

`test ! -d "{{路径/到/目录}}"`

- 如果 A 为真，则执行 B，如果出错则执行 C（请注意，即使 A 失败，C 也可能会运行）：

`test {{condition}} && {{echo "true"}} || {{echo "false"}}`

- 在条件语句中使用 `test`：

`if test -f "{{路径/到/文件}}"; then echo "文件存在"; else echo "文件不存在"; fi`
