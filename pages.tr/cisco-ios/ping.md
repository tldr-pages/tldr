# ping

> Ağ ana makinelerine ICMP ECHO_REQUEST paketleri gönder.
> Ayrıca bakınız: `mtr`.
> Daha fazla bilgi için: <https://manned.org/ping>.

- IP adresi `10.0.0.1` olan bir ana makineye ping at (Not: `10.0.0.1`, `10.1` olarak kısaltılabilir):

`ping 10.0.0.1`

- Bir ana makineye yalnızca belirli sayıda ping at:

`ping -c {{sayı}} {{ana_makine}}`

- Ana makineye ping at ve istekler arasındaki aralığı saniye cinsinden belirt (varsayılan 1 saniyedir):

`ping -i {{saniye}} {{ana_makine}}`

- Ana makineye ping at ve adresler için sembolik adları çözmeye çalışma:

`ping -n {{ana_makine}}`

- Ana makineye ping at ve bir paket alındığında zil sesi çıkar (terminaliniz destekliyorsa):

`ping -a {{ana_makine}}`

- Yanıt alınmadığında da bir mesaj göster:

`ping -O {{ana_makine}}`

- Ana makineye belirli sayıda ping at, paket başına yanıt için beklenecek süreyi ve tüm ping işleminin toplam bekleme süresi sınırını belirt:

`ping -c {{sayı}} -W {{saniye}} -w {{saniye}} {{ana_makine}}`

- Tüm IPv6 yerel ağ ana makinelerine ping at:

`ping -6 ff02::1%{{eth0}}`
