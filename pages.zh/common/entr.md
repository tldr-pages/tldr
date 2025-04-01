# entr

> 当文件更改时，运行任意命令。
> 更多信息：<https://eradman.com/entrproject/>.

- 如果任何子目录中的文件发生更改，则使用 `make` 重新构建：

`{{ag -l}} | entr {{make}}`

- 如果当前目录中的任何 `.c` 源文件发生更改，则使用 `make` 重新构建并测试：

`{{ls *.c}} | entr {{'make && make test'}}`

- 在执行 `ruby main.rb` 之前，向任何先前生成的 Ruby 子进程发送 `SIGTERM`：

`{{ls *.rb}} | entr -r {{ruby main.rb}}`

- 使用更改的文件 (`/_`) 作为参数运行命令：

`{{ls *.sql}} | entr {{psql -f}} /_`

- 在 SQL 脚本更新后，清屏并运行查询：

`{{echo my.sql}} | entr -cp {{psql -f}} /_`

- 如果源文件发生更改，则重新构建项目，并将输出限制在前几行：

`{{find src/}} | entr -s {{'make | sed 10q'}}`

- 启动并自动重新加载 Node.js 服务器：

`{{ls *.js}} | entr -r {{node app.js}}`
