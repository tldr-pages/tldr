# բեռնման թեստ

> Գործարկեք բեռնման թեստ ընտրված HTTP կամ WebSockets URL-ում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/alexfernandez/loadtest#usage>:.

- Գործարկեք միաժամանակ օգտագործողների հետ և վայրկյանում որոշակի քանակությամբ հարցումներ.:

`loadtest {{[-c|--concurrency]}} {{10}} {{[--rps|--requestsPerSecond]}} {{200}} {{https://example.com}}`

- Գործարկեք հատուկ HTTP վերնագրով.:

`loadtest --headers "{{accept:text/plain;text-html}}" {{https://example.com}}`

- Գործարկել հատուկ HTTP մեթոդով.:

`loadtest {{[-m|--method]}} {{GET}} {{https://example.com}}`
