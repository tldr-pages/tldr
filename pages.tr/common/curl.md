# curl

> Bir sunucuya veya sunucudan veri aktarır.
> HTTP, HTTPS, FTP, SCP gibi birçok protokolü destekler.
> Ayrıca bakınız: `wcurl`, `wget`.
> Daha fazla bilgi için: <https://curl.se/docs/manpage.html>.

- Bir HTTP GET isteği yap ve içeriği `stdout`'a yaz:

`curl {{https://example.com}}`

- HTTP GET isteği yap, `3xx` yönlendirmelerini takip et ve yanıt başlıklarıyla içeriği `stdout`'a yaz:

`curl {{[-L|--location]}} {{[-D|--dump-header]}} - {{https://example.com}}`

- Bir dosyayı indir ve URL'deki dosya adıyla kaydet:

`curl {{[-O|--remote-name]}} {{https://example.com/dosya.zip}}`

- Form ile kodlanmış veri gönder (`application/x-www-form-urlencoded` türünde POST isteği). `stdin`'den okumak için `--data @dosya_adı` veya `--data @'-'` kullan:

`curl {{[-X|--request]}} POST {{[-d|--data]}} '{{isim=ali}}' {{http://example.com/form}}`

- Ekstra başlık, özel HTTP yöntemi ve proxy (BurpSuite gibi) ile istek gönder, güvensiz sertifikaları yoksay:

`curl {{[-k|--insecure]}} {{[-x|--proxy]}} {{http://127.0.0.1:8080}} {{[-H|--header]}} '{{Authorization: Bearer token}}' {{[-X|--request]}} {{GET|PUT|POST|DELETE|PATCH|...}} {{https://example.com}}`

- JSON formatında veri gönder ve uygun Content-Type başlığını belirt:

`curl {{[-d|--data]}} '{{{"isim":"ali"}}}' {{[-H|--header]}} '{{Content-Type: application/json}}' {{http://example.com/users/1234}}`

- İstemci sertifikası ve özel anahtar ile istek gönder, sertifika doğrulamasını atla:

`curl {{[-E|--cert]}} {{istemci.pem}} --key {{anahtar.pem}} {{[-k|--insecure]}} {{https://example.com}}`

- Bir alan adını özel bir IP adresine çözümle, ayrıntılı çıktı ile (DNS çözümlemesi için `/etc/hosts` dosyasını düzenlemeye benzer):

`curl {{[-v|--verbose]}} --resolve {{example.com}}:{{80}}:{{127.0.0.1}} {{http://example.com}}`
