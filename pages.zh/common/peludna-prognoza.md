# 花粉预报

> 使用Pliva的过敏数据API，从终端获取克罗地亚城市的花粉测量数据。
> 更多信息：<https://github.com/vladimyr/peludna-prognoza>。

- 开始对城市进行交互式搜索并获取数据：

`peludna-prognoza`

- 获取某个城市的数据：

`peludna-prognoza "{{city}}"`

- 以机器可读格式显示数据：

`peludna-prognoza "{{city}}" --{{json|xml}}`

- 在默认网页浏览器中显示某个城市的花粉测量页面，地址为 <https://plivazdravlje.hr>：

`peludna-prognoza "{{city}}" --web`