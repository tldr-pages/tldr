# mitmweb

> Վեբ վրա հիմնված ինտերակտիվ man-in-the-middle HTTP վստահված անձ:.
> Տես նաև՝ `mitmproxy`:.
> Լրացուցիչ տեղեկություններ. <https://docs.mitmproxy.org/stable/concepts-options/>:.

- Սկսեք `mitmweb`-ը լռելյայն կարգավորումներով.:

`mitmweb`

- Սկսեք `mitmweb`՝ կապված հատուկ հասցեի և նավահանգստի հետ.:

`mitmweb --listen-host {{ip_address}} --listen-port {{port}}`

- Սկսեք `mitmweb`-ը՝ օգտագործելով սկրիպտ՝ երթևեկությունը մշակելու համար.:

`mitmweb --scripts {{path/to/script.py}}`
