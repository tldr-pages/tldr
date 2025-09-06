# dig

> DNS sunucularına sorgulama yapmak için kullanılan bir komuttur.
> Daha fazla bilgi için: <https://manned.org/dig>.

- İlgili sunucu ile ilgili IP adresi sorgulaması yapılır:

`dig +short {{example.com}}`

- DNS sorgulaması için alternatif server kullanılır:

`dig @{{1.1.1.1}} {{example.com}}`

- Tersine DNS sorgulaması yapılır:

`dig -x {{1.1.1.1}}`

- Belli başlı DNS sunucuları ile ilgili kayıtları sorgular:

`dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}`
