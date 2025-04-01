# rails

> 用 Ruby 编写的服务器端 MVC 框架。
> 一些子命令（如 `generate`）有自己的使用文档。
> 更多信息：<https://guides.rubyonrails.org/command_line.html>.

- 创建一个新的 Rails 项目：

`rails new "{{project_name}}"`

- 为名为 Post 的模型生成一个脚手架，并预定义属性 title 和 body：

`rails generate scaffold Post title:string body:text`

- 运行数据库迁移：

`rails db:migrate`

- 列出所有路由：

`rails routes`

- 在端口 3000 上为当前项目启动本地服务器：

`rails server`

- 在指定端口上为当前项目启动本地服务器：

`rails server -p "{{port}}"`

- 打开控制台以从命令行与应用程序交互：

`rails console`

- 查看当前 Rails 版本：

`rails --version`
