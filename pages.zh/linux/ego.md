# ego

> Funtoo 的官方系统个性管理工具。
> 更多信息：<https://funtoo-ego.readthedocs.io/en/develop/>.

- 同步 Portage 树：

`ego sync`

- 更新引导加载程序配置：

`ego boot update`

- 通过名称阅读 Funtoo 维基页面：

`ego doc {{wiki_page}}`

- 打印当前配置文件：

`ego profile show`

- 启用/禁用混入：

`ego profile mix-in +{{gnome}} -{{kde-plasma-5}}`

- 查询与指定软件包相关的 Funtoo 错误：

`ego query bug {{package}}`
