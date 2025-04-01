# kosmorro

> 计算地球上某个位置在某日期的星象和事件。
> 更多信息：<https://kosmorro.space>.

- 获取法国巴黎的星象：

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}}`

- 获取法国巴黎在UTC+2时区的星象：

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}} --timezone={{2}}`

- 获取2020年6月9日法国巴黎的星象：

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}} --date={{2020-06-09}}`

- 生成PDF（注：必须安装TeXLive）：

`kosmorro --format={{pdf}} --output={{path/to/file.pdf}}`
