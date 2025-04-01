# test

> 检查文件类型和比较值。
> 如果条件为真，则返回 0；如果条件为假，则返回 1。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/test-invocation.html>.

- 测试给定变量是否等于给定字符串：

`test "{{$MY_VAR}}" = "{{/bin/zsh}}"`

- 测试给定变量是否为空：

`test -z "{{$GIT_BRANCH}}"`

- 测试文件是否存在：

`test -f "{{path/to/file_or_directory}}"`

- 测试目录是否不存在：

`test ! -d "{{path/to/directory}}"`

- 如果 A 为真，则执行 B；如果 A 为假或出错，则执行 C：

`test {{condition}} && {{echo "true"}} || {{echo "false"}}`