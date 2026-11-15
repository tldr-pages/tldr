# man

> Kılavuz sayfalarını biçimlendir ve göster.
> Ayrıca bakınız: `whatis`, `apropos`.
> Daha fazla bilgi için: <https://manned.org/man>.

- Bir komut için man sayfasını görüntüle:

`man {{komut}}`

- Bir komutun man sayfasını tarayıcıda aç (`$BROWSER` ayarlıysa `=tarayıcı_adı` atlanabilir):

`man {{[-H|--html=]}}{{tarayıcı_adı}} {{komut}}`

- Bir komut için man sayfasını 7. bölümden görüntüle:

`man 7 {{komut}}`

- Bir komut için kullanılabilir tüm bölümleri listele:

`man {{[-f|--whatis]}} {{komut}}`

- Man sayfaları için aranan yolu göster:

`man {{[-w|--path]}}`

- Man sayfasını göstermek yerine man sayfasının konumunu göster:

`man {{[-w|--where]}} {{komut}}`

- Man sayfasını belirli bir yerel ayarla (locale) görüntüle:

`man {{[-L|--locale]}} {{yerel_ayar}} {{komut}}`

- Belirtilen ifadeyi içeren man sayfalarını ara:

`man {{[-k|--apropos]}} "{{aranan_ifade}}"`
