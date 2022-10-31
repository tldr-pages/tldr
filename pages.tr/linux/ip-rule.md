# ip rule

> IP yönlendirme politikası veri tabanı yönetimi.
> Daha fazla bilgi için: <https://man7.org/linux/man-pages/man8/ip-rule.8.html>.

- Yönlendirme politikasını göster:

`ip rule {{show|list}}`

- Paket kaynak adreslerine dayalı yeni bir kural ekle:

`sudo ip rule add from {{192.168.178.2/32}}`

- Paket hedef adreslerine dayalı yeni bir kural ekle:

`sudo ip rule add to {{192.168.178.2/32}}`

- Paket kaynak adreslerine dayalı bir kuralı sil:

`sudo ip rule delete from {{192.168.178.2/32}}`

- Paket hedef adreslerine dayalı bir kuralı sil:

`sudo ip rule delete to {{192.168.178.2/32}}`

- Silinen tüm kuralları temizle:

`ip rule flush`

- Tüm kuralları bir dosyaya kaydet:

`ip rule save > {{ip_kuralları.dat/dosyasının/yolu}}`

- Tüm kuralları bir dosyadan geri yükle:

`ip rule restore < {{ip_kuralları.dat/dosyasının/yolu}}`
