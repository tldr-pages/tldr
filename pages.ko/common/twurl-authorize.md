# twurl authorize

> Twitter API 자격 증명을 사용하여 twurl을 인증.
> 더 많은 정보: <https://github.com/twitter/twurl>.

- Consumer Key와 Consumer Secret을 사용하여 twurl 인증:

`twurl authorize {{[-c|--consumer-key]}} {{consumer_키}} {{[-s|--consumer-secret]}} {{consumer_시크릿}}`

- Consumer Key와 Consumer Secret을 사용하여 twurl을 인증하고, 브라우저에서 인증 URL 열기:

`twurl authorize {{[-c|--consumer-key]}} {{consumer_키}} {{[-s|--consumer-secret]}} {{consumer_시크릿}} --open`

- 지정한 호스트에 대해 twurl 인증:

`twurl authorize {{[-c|--consumer-key]}} {{consumer_키}} {{[-s|--consumer-secret]}} {{consumer_시크릿}} {{[-H|--host]}} {{api.twitter.com}}`
