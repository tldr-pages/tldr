# ip rule

> IP yönlendirme politikası veri tabanı yönetimi.
> Daha fazla bilgi için: <https://manned.org/ip-rule>.

- Yönlendirme politikasını göster:

`ip {{[ru|rule]}} {{show|list}}`

- Paket kaynak adreslerine dayalı yeni bir kural ekle:

`sudo ip {{[ru|rule]}} add from {{192.168.178.2/32}}`

- Paket hedef adreslerine dayalı yeni bir kural ekle:

`sudo ip {{[ru|rule]}} add to {{192.168.178.2/32}}`

- Paket kaynak adreslerine dayalı bir kuralı sil:

`sudo ip {{[ru|rule]}} delete from {{192.168.178.2/32}}`

- Paket hedef adreslerine dayalı bir kuralı sil:

`sudo ip {{[ru|rule]}} delete to {{192.168.178.2/32}}`

- Silinen tüm kuralları temizle:

`ip {{[ru|rule]}} flush`

- Tüm kuralları bir dosyaya kaydet:

`ip {{[ru|rule]}} save > {{ip_kuralları.dat/dosyasının/yolu}}`

- Tüm kuralları bir dosyadan geri yükle:

`ip {{[ru|rule]}} restore < {{ip_kuralları.dat/dosyasının/yolu}}`
