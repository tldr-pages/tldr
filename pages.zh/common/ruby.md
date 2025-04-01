# ruby

> Ruby 编程语言解释器。
> 参见: `gem`, `bundler`, `rake`, `irb`。
> 更多信息: <https://www.ruby-lang.org>。

- 执行 Ruby 脚本：

`ruby {{script.rb}}`

- 在命令行中执行单个 Ruby 命令：

`ruby -e {{command}}`

- 检查给定的 Ruby 脚本是否有语法错误：

`ruby -c {{script.rb}}`

- 在当前目录下启动内置的 HTTP 服务器，端口号为 8080：

`ruby -run -e httpd`

- 本地执行一个 Ruby 可执行文件，而不安装其依赖的库：

`ruby -I {{path/to/library_folder}} -r {{library_require_name}} {{path/to/bin_folder/bin_name}}`

- 显示 Ruby 版本：

`ruby -v`