# collectd

> 系统统计数据收集守护进程。
> 更多信息：<https://collectd.org/>.

- 测试配置文件，然后退出：

`collectd -t`

- 测试插件数据收集功能，然后退出：

`collectd -T`

- 启动 `collectd`：

`collectd`

- 指定自定义配置文件位置：

`collectd -C {{path/to/file}}`

- 指定自定义 PID 文件位置：

`collectd -P {{path/to/file}}`

- 不要在后台运行：

`collectd -f`

- 显示帮助和版本信息：

`collectd -h`