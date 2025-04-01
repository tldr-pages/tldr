# peludna-prognoza

> 从终端使用 Pliva 的过敏数据 API 获取克罗地亚城市的花粉测量数据。
> 更多信息：<https://github.com/vladimyr/peludna-prognoza>.

- 启动交互式城市搜索并获取数据：

`peludna-prognoza`

- 获取指定城市的花粉数据：

`peludna-prognoza "{{city}}"`

- 以机器可读格式显示数据：

`peludna-prognoza "{{city}}" --{{json|xml}}`

- 在默认网页浏览器中显示 <https://plivazdravlje.hr> 上指定城市的花粉测量页面：

`peludna-prognoza "{{city}}" --web`
