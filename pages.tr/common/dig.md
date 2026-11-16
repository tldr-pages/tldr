# dig

> DNS sunucularına sorgulama yapmak için kullanılan bir komuttur.
> Ayrıca bakınız: `resolvectl`, `nslookup`, `host`.
> Daha fazla bilgi için: <https://manned.org/dig>.

- Bir ana bilgisayar adıyla ilişkili IP adres(ler)ini sorgula (A kayıtları):

`dig +short {{example.com}}`

- Belirli bir alan adı için ayrıntılı bir yanıt al (A kayıtları):

`dig +noall +answer {{example.com}}`

- Belirli bir alan adıyla ilişkili belirli bir DNS kaydı türünü sorgula:

`dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}`

- Sorgulanacak alternatif bir DNS sunucusu belirt ve isteğe bağlı olarak TLS üzerinden DNS (DoT) kullan:

`dig {{+tls}} @{{1.1.1.1|8.8.8.8|9.9.9.9|...}} {{example.com}}`

- Bir IP adresi için tersine DNS sorgulaması yap (PTR kaydı):

`dig -x {{8.8.8.8}}`

- Bölgenin yetkili ad sunucularını bul ve SOA kayıtlarını görüntüle:

`dig +nssearch {{example.com}}`

- İteratif sorgular yap ve bir alan adını çözümlemek için izlenen yolun tamamını görüntüle:

`dig +trace {{example.com}}`

- Standart olmayan bir [p]ort üzerinden TCP protokolünü kullanarak bir DNS sunucusunu sorgula:

`dig +tcp -p {{port}} @{{dns_sunucusu_ip}} {{example.com}}`
