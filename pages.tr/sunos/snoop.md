# snoop

> Ağ paketi inceleyici.
> SunOS'in tcpdump alternatifi.
> Daha fazla bilgi için: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Belirtilen ağ arayüzünde paketleri yakala:

`snoop -d {{e1000g0}}`

- Yakalanan paketleri terminalde göstermek yerine bir dosyaya kaydet:

`snoop -o {{dosyaismi}}`

- Belirtilen dosyadan paketlerin ayrıntılı protokol katman özetini görüntüle:

`snoop -V -i {{dosyaismi}}`

- Host isminden gelen ağ paketlerini yakala ve belirtilen port'a git:

`snoop to port {{port}} from host {{hostismi}}`

- İki IP adresi arasında takas edilen ağ paketleriini yakala ve hex değerlerini göster:

`snoop -x0 -p4 {{ip_addresi_1}} {{ip_addresi_2}}`
