# http

> HTTPie. HTTP հաճախորդ, որը նախատեսված է փորձարկման, վրիպազերծման և ընդհանրապես API-ների և HTTP սերվերների հետ փոխազդելու համար:.
> Տես նաև՝ `xh`:.
> Լրացուցիչ տեղեկություններ. <https://httpie.io/docs/cli/usage>:.

- Կատարեք պարզ GET հարցում (ցույց է տալիս պատասխանի վերնագրերը և բովանդակությունը).:

`http {{https://example.com}}`

- Տպել բովանդակության որոշակի հատվածներ (`H`՝ հարցումների վերնագրեր, `B`՝ հարցումների հիմնական մասը, `h`՝ պատասխանի վերնագրեր, `b`՝ պատասխանի մարմին, `m`՝ պատասխանի մետատվյալներ):

`http {{[-p|--print]}} {{H|B|h|b|m|Hh|Hhb|...}} {{https://example.com}}`

- Հարցում ուղարկելիս նշեք HTTP մեթոդը և օգտագործեք վստահված անձ՝ հարցումն ընդհատելու համար.:

`http {{GET|POST|HEAD|PUT|PATCH|DELETE|...}} --proxy {{http|https}}:{{http://localhost:8080|socks5://localhost:9050|...}} {{https://example.com}}`

- Հետևեք `3xx` վերահղումներին և հարցումում նշեք լրացուցիչ վերնագրեր.:

`http {{[-F|--follow]}} {{https://example.com}} {{'User-Agent: Mozilla/5.0' 'Accept-Encoding: gzip'}}`

- Նույնականացում սերվերի վրա՝ օգտագործելով նույնականացման տարբեր մեթոդներ.:

`http {{[-a|--auth]}} {{username:password|token}} {{[-A|--auth-type]}} {{basic|digest|bearer}} {{GET|POST|...}} {{https://example.com/auth}}`

- Ստեղծեք հարցում, բայց մի ուղարկեք այն (նման է չոր վազքի).:

`http --offline {{GET|DELETE|...}} {{https://example.com}}`

- Օգտագործեք անվանված նիստերը մշտական մաքսային վերնագրերի, վավերականության հավաստագրերի և թխուկների համար.:

`http --session {{session_name|path/to/session.json}} {{[-a|--auth]}} {{username}}:{{password}} {{https://example.com/auth}} {{API-KEY:xxx}}`

- Վերբեռնեք ֆայլ ձևի մեջ (ներքևի օրինակը ենթադրում է, որ ձևի դաշտը `<input type="file" name="cv" />` է):

`http {{[-f|--form]}} {{POST}} {{https://example.com/upload}} {{cv@path/to/file}}`
