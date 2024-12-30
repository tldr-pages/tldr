# surge

> 简单的网站发布。
> 更多信息：<https://surge.sh>。

- 上传新网站到 surge.sh：

`surge {{path/to/my_project}}`

- 将网站部署到自定义域名（请注意，DNS 记录必须指向 surge.sh 子域名）：

`surge {{path/to/my_project}} {{my_custom_domain.com}}`

- 列出你的 surge 项目：

`surge list`

- 移除一个项目：

`surge teardown {{my_custom_domain.com}}`