# nginx

> Nginx web sunucusu.
> Daha fazla bilgi: <https://nginx.org/en/>.

- Varsayılan konfigürasyon dosyasıyla sunucuyu başlat:

`nginx`

- Özel bir konfigürasyon dosyasıyla sunucuyu başlat:

`nginx -c {{konfigürasyon_dosyası}}`

- Konfigürasyon dosyasındaki her göreceli dosya yolu için bir ön ek ile sunucuyu başlat:

`nginx -c {{konfigürasyon_dosyası}} -p {{göreceli/dosya/yolu/ön/eki}}`

- Çalışan sunucuyu etkilemeden konfigürasyon dosyasını test et:

`nginx -t`

- Aksamasız bir sinyal göndererek konfigürasyonu tekrar yükle:

`nginx -s reload`
