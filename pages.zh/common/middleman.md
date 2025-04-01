# middleman

> 用 Ruby 编写的静态站点生成器。
> 更多信息：<https://middlemanapp.com/>.

- 创建一个新的 Middleman 项目：

`middleman init "{{project_name}}"`

- 在本地启动当前项目的服务器，端口为 4567：

`middleman server`

- 在指定的端口上为当前项目启动本地服务器：

`middleman server -p "{{port}}"`

- 构建当前目录中的项目以准备部署：

`bundle exec middleman build`

- 部署当前目录中的 Middleman 项目：

`middleman deploy`