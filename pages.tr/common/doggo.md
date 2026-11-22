# doggo

> İnsanlar için modern DNS istemcisi.
> Golang ile yazılmıştır.
> Daha fazla bilgi: <https://github.com/mr-karan/doggo/blob/main/docs/src/content/docs/guide/reference.md>.

- Basit bir DNS sorgusu gerçekleştir:

`doggo {{example.com}}`

- Belirli bir ad sunucusunu kullanarak MX kayıtlarını sorgula:

`doggo MX {{codeberg.org}} @{{1.1.1.2}}`

- HTTPS üzerinden DNS (DoH) kullan:

`doggo {{example.com}} @{{https://dns.quad9.net/dns-query}}`

- Çıktıyı JSON biçiminde göster:

`doggo {{example.com}} {{[-J|--json]}} | jq '{{.responses[0].answers[].address}}'`

- IP adresi için ters DNS sorgusu yap:

`doggo {{[-x|--reverse]}} {{8.8.4.4}} --short`
