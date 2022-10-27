# varnishlog

> Display Varnish logs.
> More information: <https://varnish-cache.org/docs/trunk/reference/varnishlog.html>.

- Display logs in real time:

`varnishlog`

- Only display requests to a specific domain:

`varnishlog -q 'ReqHeader eq "Host: {{example.com}}"'`

- Only display POST requests:

`varnishlog -q 'ReqMethod eq "{{POST}}"'`

- Only display requests to a specific path:

`varnishlog -q 'ReqURL eq "{{/path}}"'`

- Only display requests to paths matching a regular expression:

`varnishlog -q 'ReqURL ~ "{{regex}}"'`
