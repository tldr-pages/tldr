# croc

> Herhangi bir ağ üzerinden dosyaları kolayca ve güvenli bir şekilde gönderin ve alın.
> Daha fazla bilgi: <https://github.com/schollz/croc>.

- Bir dosya veya dizin gönder:

`croc send {{dosya_veya_dizin_yolu}}`

- Belirli bir parola ile bir dosya veya dizin gönder:

`croc send {{[-c|--code]}} {{parola}} {{dosya_veya_dizin_yolu}}`

- Alıcı makinede bir dosya veya dizin al:

`croc {{parola}}`

- Özel bir röle (relay) üzerinden gönder ve bağlan:

`croc --relay {{röle_ip_adresi}} send {{dosya_veya_dizin_yolu}}`

- Özel bir röle üzerinden al ve bağlan:

`croc --relay {{röle_ip_adresi}} {{parola}}`

- Varsayılan bağlantı noktalarında bir croc rölesi barındır:

`croc relay`

- Bir croc komutu için parametreleri ve seçenekleri görüntüle:

`croc {{send|relay}} --help`
