# kosmorro

> 计算某个日期在地球上某个位置的天文历和事件。
> 更多信息：<https://kosmorro.space>。

- 获取法国巴黎的天文历：

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}}`

- 获取法国巴黎的天文历，使用 UTC+2 时区：

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}} --timezone={{2}}`

- 获取法国巴黎在2020年6月9日的天文历：

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}} --date={{2020-06-09}}`

- 生成 PDF（注意：必须安装 TeXLive）：

`kosmorro --format={{pdf}} --output={{path/to/file.pdf}}`