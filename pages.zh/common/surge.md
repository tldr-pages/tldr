# surge

> 简单的网页发布工具。
> 更多信息：<https://surge.sh>。

- 将新站点上传到 surge.sh：

`surge {{path/to/my_project}}`

- 将站点部署到自定义域名（注意：DNS 记录必须指向 surge.sh 子域名）：

`surge {{path/to/my_project}} {{my_custom_domain.com}}`

- 列出你的 surge 项目：

`surge list`

- 删除一个项目：

`surge teardown {{my_custom_domain.com}}`