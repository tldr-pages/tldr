# 中介

> 用Ruby编写的静态网站生成器。
> 更多信息：<https://middlemanapp.com/>。

- 创建一个新的Middleman项目：

`middleman init "{{project_name}}"`

- 在4567端口上启动当前项目的本地服务器：

`middleman server`

- 在指定端口上启动当前项目的本地服务器：

`middleman server -p "{{port}}"`

- 构建当前目录中的项目以准备部署：

`bundle exec middleman build`

- 部署当前目录中的Middleman项目：

`middleman deploy`