# 测试

> 检查文件类型并比较值。
> 如果条件评估为真，则返回0；如果评估为假，则返回1。
> 更多信息：<https://www.gnu.org/software/coreutils/test>。

- 测试给定变量是否等于给定字符串：

`test "{{$MY_VAR}}" = "{{/bin/zsh}}"`

- 测试给定变量是否为空：

`test -z "{{$GIT_BRANCH}}"`

- 测试文件是否存在：

`test -f "{{path/to/file_or_directory}}"`

- 测试目录是否不存在：

`test ! -d "{{path/to/directory}}"`

- 如果A为真，则执行B，或在错误情况下执行C（注意即使A失败，C也可能会执行）：

`test {{condition}} && {{echo "true"}} || {{echo "false"}}`