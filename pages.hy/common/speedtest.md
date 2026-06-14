# արագության թեստ

> Պաշտոնական հրամանի տող ինտերֆեյս ինտերնետի թողունակությունը ստուգելու համար՝ օգտագործելով <https://speedtest.net>-ը:.
> Նշում. որոշ հարթակներ կապում են `speedtest`-ին `speedtest-cli`-ին կամ այլ գործիքներին, ինչպիսիք են `librespeed`-ը, որոնք կարող են տեղադրվել նաև որպես `speedtest` որոշ Linux բաշխումների վրա:.
> Այս հրամանների օրինակները վերաբերում են միայն պաշտոնական հաճախորդին:.
> Լրացուցիչ տեղեկություններ. <https://www.speedtest.net/apps/cli>:.

- Արագության թեստ կատարեք.:

`speedtest`

- Կատարեք արագության թեստ և նշեք ելքի միավորը.:

`speedtest {{[-u|--unit]}} {{auto-decimal-bits|auto-decimal-bytes|auto-binary-bits|auto-binary-bytes}}`

- Գործարկեք արագության թեստ և նշեք ելքային ձևաչափը.:

`speedtest {{[-f|--format]}} {{human-readable|csv|tsv|json|jsonl|json-pretty}}`

- Գործարկեք արագության թեստ և նշեք օգտագործվող տասնորդական միավորների քանակը (0-ից 8, լռելյայն՝ 2):

`speedtest {{[-P|--precision]}} {{precision}}`

- Կատարեք արագության թեստ և տպեք դրա առաջընթացը (հասանելի է միայն `human-readable` և `json` ելքային ձևաչափերի համար):

`speedtest {{[-p|--progress]}} {{yes|no}}`

- Նշեք բոլոր `speedtest.net` սերվերները՝ դասավորված ըստ հեռավորության.:

`speedtest {{[-L|--servers]}}`

- Արագության փորձարկում կատարեք կոնկրետ `speedtest.net` սերվերի վրա.:

`speedtest {{[-s|--server-id]}} {{server_id}}`
