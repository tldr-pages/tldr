# varnishlog

> 显示 Varnish 日志。
> 更多信息：<https://varnish-cache.org/docs/trunk/reference/varnishlog.html>。

- 实时显示日志：

`varnishlog`

- 仅显示对特定域名的请求：

`varnishlog -q 'ReqHeader eq "Host: {{example.com}}"'`

- 仅显示 POST 请求：

`varnishlog -q 'ReqMethod eq "{{POST}}"'`

- 仅显示对特定路径的请求：

`varnishlog -q 'ReqURL eq "{{/path}}"'`

- 仅显示匹配正则表达式的路径请求：

`varnishlog -q 'ReqURL ~ "{{regex}}"'`
