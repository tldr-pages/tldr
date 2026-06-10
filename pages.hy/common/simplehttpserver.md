# պարզhttpսերվեր

> Պարզ HTTP/S սերվեր, որն աջակցում է ֆայլերի վերբեռնմանը, հիմնական իսկորոշմանը և YAML կանոններին հատուկ պատասխանների համար:.
> Python-ի `http.server`-ին այլընտրանք Go:.
> Լրացուցիչ տեղեկություններ. <https://github.com/projectdiscovery/simplehttpserver>:.

- Գործարկեք HTTP սերվերը, որը սպասարկում է ընթացիկ գրացուցակը մանրամասն ելքով (լսեք բոլոր ինտերֆեյսներով և 8000 նավահանգստով ըստ լռելյայն).:

`simplehttpserver -verbose`

- Սկսեք HTTP սերվերը հիմնական նույնականացումով, որը սպասարկում է հատուկ ուղի 80 նավահանգստի վրա բոլոր ինտերֆեյսներում.:

`sudo simplehttpserver -basic-auth {{username}}:{{password}} -path {{/var/www/html}} -listen 0.0.0.0:80`

- Գործարկեք HTTP սերվերը, հնարավորություն տալով HTTPS-ին, օգտագործելով ինքնաստորագրված վկայականը հատուկ SAN-ով բոլոր ինտերֆեյսներում.:

`sudo simplehttpserver -https -domain {{*.selfsigned.com}} -listen 0.0.0.0:443`

- Սկսեք HTTP սերվերը հատուկ պատասխանների վերնագրերով և վերբեռնման հնարավորությամբ.:

`simplehttpserver -upload -header '{{X-Powered-By: Go}}' -header '{{Server: SimpleHTTPServer}}'`

- Սկսեք HTTP սերվերը YAML-ում կարգավորելի կանոններով (տես DSL-ի փաստաթղթերը).:

`simplehttpserver -rules {{rules.yaml}}`
