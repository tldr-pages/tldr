# mitmdump

> Դիտեք, գրանցեք և ծրագրային կերպով փոխակերպեք HTTP տրաֆիկը:.
> mitmproxy-ի հրամանի տողի նմանակը:.
> Լրացուցիչ տեղեկություններ. <https://docs.mitmproxy.org/stable/#mitmdump>:.

- Գործարկեք վստահված անձ և պահեք բոլոր արդյունքները ֆայլում.:

`mitmdump {{[-w|--wfile]}} {{path/to/file}}`

- Զտեք պահպանված երթևեկության ֆայլը միայն POST հարցումների համար.:

`mitmdump {{[-nr|--no-server --read-flows]}} {{input_filename}} {{[-w|--wfile]}} {{output_filename}} "{{~m post}}"`

- Կրկնել պահպանված երթևեկության ֆայլը.:

`mitmdump {{[-nc|--no-server --client-replay]}} {{path/to/file}}`

- Ընդհատել DNS տրաֆիկը (սկսում է ընդհատող DNS սերվերը 127.0.0.1:53):

`sudo mitmdump {{[-m|--mode]}} dns`
