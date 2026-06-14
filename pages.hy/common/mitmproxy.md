# mitmproxy

> Ինտերակտիվ մարդ-միջին HTTP վստահված անձ:.
> Տես նաև՝ `mitmweb`, `mitmdump`:.
> Լրացուցիչ տեղեկություններ. <https://docs.mitmproxy.org/stable/>:.

- Սկսեք `mitmproxy`-ը լռելյայն կարգավորումներով (կլսվի `8080` նավահանգստում):

`mitmproxy`

- Սկսեք `mitmproxy`՝ կապված հատուկ հասցեի և միացքի հետ.:

`mitmproxy --listen-host {{ip_address}} {{[-p|--listen-port]}} {{port}}`

- Սկսեք `mitmproxy`-ն՝ օգտագործելով սկրիպտ՝ երթևեկությունը մշակելու համար.:

`mitmproxy {{[-s|--scripts]}} {{path/to/script.py}}`

- Արտահանել տեղեկամատյանները SSL/TLS հիմնական ստեղներով արտաքին ծրագրեր (wireshark և այլն):

`SSLKEYLOGFILE="{{path/to/file}}" mitmproxy`

- Նշեք պրոքսի սերվերի աշխատանքի ռեժիմը (`regular` լռելյայն է).:

`mitmproxy {{[-m|--mode]}} {{regular|transparent|socks5|...}}`

- Սահմանեք վահանակի դասավորությունը.:

`mitmproxy --console-layout {{horizontal|single|vertical}}`

- Պահպանեք ամբողջ վստահված տրաֆիկը ֆայլում՝ հետագա վերլուծության համար.:

`mitmproxy {{[-w|--save-stream-file]}} {{path/to/dump.mitm}}`

- Վերարտադրեք նախկինում պահպանված HTTP հոսքի ֆայլը.:

`mitmproxy {{[-nr|--no-server --rfile]}} {{path/to/dump.mitm}}`
