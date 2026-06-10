# կապի ստուգիչ

> Հաճախորդը ստուգելու HTML փաստաթղթերը և կայքերը կոտրված հղումների համար:.
> Լրացուցիչ տեղեկություններ. <https://linkchecker.github.io/linkchecker/man/linkchecker.html>:.

- Գտեք կոտրված հղումներ <https://example.com/> կայքում:

`linkchecker {{https://example.com/}}`

- Նաև ստուգեք URL-ները, որոնք ուղղված են դեպի արտաքին տիրույթներ.:

`linkchecker --check-extern {{https://example.com/}}`

- Անտեսեք URL-ները, որոնք համապատասխանում են որոշակի `regex`-ին.:

`linkchecker --ignore-url {{regex}} {{https://example.com/}}`

- Արդյունքները թողարկեք CSV ֆայլ.:

`linkchecker --file-output {{csv}}/{{path/to/file}} {{https://example.com/}}`
