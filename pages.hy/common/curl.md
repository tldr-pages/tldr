#գանգուր

> Տվյալների փոխանցում սերվերից կամ սերվերից:.
> Աջակցում է արձանագրությունների մեծամասնությանը, ներառյալ HTTP, HTTPS, FTP, SCP և այլն:.
> Տես նաև՝ `wcurl`, `wget`:.
> Լրացուցիչ տեղեկություններ. <https://curl.se/docs/manpage.html>:.

- Կատարեք HTTP GET հարցում և թափեք բովանդակությունը `stdout`-ում:

`curl {{https://example.com}}`

- Կատարեք HTTP GET հարցում, հետևեք `3xx` վերահղումներին և պատասխանի վերնագրերն ու բովանդակությունը թողեք `stdout`:

`curl {{[-L|--location]}} {{[-D|--dump-header]}} - {{https://example.com}}`

- Ներբեռնեք ֆայլ՝ ելքը պահպանելով URL-ով նշված ֆայլի անվան տակ.:

`curl {{[-O|--remote-name]}} {{https://example.com/filename.zip}}`

- Ուղարկեք ձևի կոդավորված տվյալներ (POST հարցում՝ տիպի `application/x-www-form-urlencoded`): Օգտագործեք `--data @file_name` կամ `--data @'-'`՝ `stdin`-ից կարդալու համար:

`curl {{[-X|--request]}} POST {{[-d|--data]}} '{{name=bob}}' {{http://example.com/form}}`

- Ուղարկեք հարցում հավելյալ վերնագրով՝ օգտագործելով հատուկ HTTP մեթոդ և վստահված անձի միջոցով (օրինակ՝ BurpSuite)՝ անտեսելով անապահով ինքնաստորագրված վկայագրերը.:

`curl {{[-k|--insecure]}} {{[-x|--proxy]}} {{http://127.0.0.1:8080}} {{[-H|--header]}} '{{Authorization: Bearer token}}' {{[-X|--request]}} {{GET|PUT|POST|DELETE|PATCH|...}} {{https://example.com}}`

- Ուղարկեք տվյալները JSON ձևաչափով, նշելով համապատասխան Content-Type վերնագիրը.:

`curl {{[-d|--data]}} '{{{"name":"bob"}}}' {{[-H|--header]}} '{{Content-Type: application/json}}' {{http://example.com/users/1234}}`

- Անցեք հաճախորդի վկայականը և հարցման մասնավոր բանալին՝ բաց թողնելով վկայագրի վավերացումը.:

`curl {{[-E|--cert]}} {{client.pem}} --key {{key.pem}} {{[-k|--insecure]}} {{https://example.com}}`

- Հոսթի անունը լուծեք անհատականացված IP հասցեով, մանրամասն ելքով (նման է `/etc/hosts` ֆայլի խմբագրմանը հատուկ DNS լուծման համար):

`curl {{[-v|--verbose]}} --resolve {{example.com}}:{{80}}:{{127.0.0.1}} {{http://example.com}}`
