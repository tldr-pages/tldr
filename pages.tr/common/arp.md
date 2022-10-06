# arp

> Sistemin ARP önbelleğini görüntüle ve manipüle et.
> Daha fazla bilgi: <https://manned.org/arp>.

- Mevcut ARP tablosunu göster:

`arp -a`

- Tüm önbelleği temizle:

`sudo arp -a -d`

- Belirli bir girdiyi sil:

`arp -d {{address}}`

- ARP tablosunda bir girdi oluştur:

`arp -s {{address}} {{mac_address}}`
