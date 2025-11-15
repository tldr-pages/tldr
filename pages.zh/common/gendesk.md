# gendesk

> 通过指定少量信息的命令来生成`.desktop`文件以及下载图标。
> 更多信息：<https://manned.org/gendesk>.

- 创建一个名为`应用程序`的`.desktop`文件：

`gendesk -n --name "{{应用程序}}" --exec "{{/路径/到/应用程序}}" --icon "{{/路径/到/图标.png}}" --comment "{{这是一个应用程序}}"`

- 创建一个名为`应用程序`的`.desktop`文件, 不显示任何输出，如果存在则覆盖同名文件：

`gendesk -q -f -n --name "{{应用程序}}" --exec "{{/路径/到/应用程序}}" --icon "{{/路径/到/图标.png}}" --comment "{{这是一个应用程序}}"`

- 显示帮助信息：

`gendesk -h`
