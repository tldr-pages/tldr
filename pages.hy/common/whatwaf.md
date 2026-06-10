# whatwaf

> Հայտնաբերել և շրջանցել վեբ հավելվածների firewalls-ը և պաշտպանության համակարգերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Ekultek/WhatWaf#basic-help-menu>:.

- Հայտնաբերեք պաշտպանությունը մեկ URL-ի վրա, կամայականորեն օգտագործեք մանրամասն ելք.:

`whatwaf {{[-u|--url]}} {{https://example.com}} --verbose`

- Հայտնաբերել պաշտպանությունը ֆայլից զուգահեռ URL-ների ցանկում (մեկ URL յուրաքանչյուր տողում).:

`whatwaf {{[-t|--threads]}} {{number}} {{[-l|--list]}} {{path/to/file}}`

- Ուղարկեք հարցումներ վստահված անձի միջոցով և օգտագործեք ֆայլից մաքսային բեռների ցուցակը (մեկ բեռ յուրաքանչյուր տողում).:

`whatwaf --proxy {{http://127.0.0.1:8080}} --pl {{path/to/file}} {{[-u|--url]}} {{https://example.com}}`

- Ուղարկեք հարցումներ Tor-ի միջոցով (Tor-ը պետք է տեղադրվի)՝ օգտագործելով մաքսային բեռներ (ստորակետերով բաժանված).:

`whatwaf --tor {{[-p|--payloads]}} '{{payload1,payload2,...}}' {{[-u|--url]}} {{https://example.com}}`

- Օգտագործեք պատահական օգտագործող-գործակալ, սահմանեք throttling և timeout, ուղարկեք POST հարցում և ստիպեք HTTPS կապը.:

`whatwaf --ra --throttle {{seconds}} --timeout {{seconds}} {{[-P|--post]}} --force-ssl {{[-u|--url]}} {{http://example.com}}`

- Թվարկեք բոլոր WAF-ները, որոնք կարող են հայտնաբերվել.:

`whatwaf --wafs`

- Թվարկեք բոլոր հասանելի կեղծ սցենարները.:

`whatwaf --tampers`
