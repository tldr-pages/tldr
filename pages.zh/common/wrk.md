# wrk

> HTTP 基准测试工具。
> 更多信息：<https://github.com/wg/wrk>.

- 运行一个持续 `30` 秒、使用 `12` 个线程并保持 `400` 个 HTTP 连接打开的基准测试：

`wrk -t{{12}} -c{{400}} -d{{30s}} "{{http://127.0.0.1:8080/index.html}}"`

- 运行一个带有自定义头部的基准测试：

`wrk -t{{2}} -c{{5}} -d{{5s}} -H "{{Host: example.com}}" "{{http://example.com/index.html}}"`

- 运行一个请求超时时间为 `2` 秒的基准测试：

`wrk -t{{2}} -c{{5}} -d{{5s}} --timeout {{2s}} "{{http://example.com/index.html}}"`