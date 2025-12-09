# varnishlog

> Varnish 로그 표시.
> 더 많은 정보: <https://varnish-cache.org/docs/trunk/reference/varnishlog.html>.

- 실시간으로 로그 표시:

`varnishlog`

- 특정 도메인에 대한 요청만 표시:

`varnishlog -q 'ReqHeader eq "Host: {{example.com}}"'`

- POST 요청만 표시:

`varnishlog -q 'ReqMethod eq "{{POST}}"'`

- 특정 경로에 대한 요청만 표시:

`varnishlog -q 'ReqURL eq "{{/경로}}"'`

- 정규 표현식과 일치하는 경로에 대한 요청만 표시:

`varnishlog -q 'ReqURL ~ "{{정규표현식}}"'`
