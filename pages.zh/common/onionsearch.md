# onionsearch

> 抓取不同 `.onion` 搜索引擎上的 URL。
> 注意：`onionsearch` 需要在 `localhost:9050` 上运行 Tor 代理；需要一个支持 Tor 的浏览器来访问 `.onion` 网站。
> 更多信息：<https://github.com/megadose/OnionSearch>。

- 从所有搜索引擎请求结果：

`onionsearch "{{string}}"`

- 从特定搜索引擎请求搜索结果：

`onionsearch "{{string}}" --engines {{tor66 deeplink phobos ...}}`

- 在搜索时排除某些搜索引擎：

`onionsearch "{{string}}" --exclude {{candle ahmia ...}}`

- 限制每个引擎加载的页面数量：

`onionsearch "{{stuxnet}}" --engines {{tor66 deeplink phobos ...}} --limit {{3}}`

- 列出所有支持的搜索引擎：

`onionsearch --help | grep -A1 -i "supported engines"`