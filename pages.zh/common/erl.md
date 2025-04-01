# erl

> 运行和管理 Erlang 编程语言中的程序。
> 更多信息：<https://www.erlang.org>。

- 编译并以普通脚本方式运行顺序的 Erlang 程序，然后退出：

`erlc {{path/to/file1 path/to/file2 ...}} && erl -noshell '{{mymodule:myfunction(arguments)}}, init:stop().'`

- 连接到正在运行的 Erlang 节点：

`erl -remsh {{nodename}}@{{hostname}} -sname {{custom_shortname}} -hidden -setcookie {{cookie_of_remote_node}}`

- 告诉 Erlang shell 从目录加载模块：

`erl -pa {{path/to/directory_with_beam_files}}`