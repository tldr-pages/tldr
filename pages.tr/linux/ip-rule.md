# ip rule

> IP yönlendirme politikası veri tabanı yönetimi.
> Daha fazla bilgi için: <https://manned.org/ip-rule>.

- Yönlendirme politikasını göster:

`ip {{[ru|rule]}}`

- Paket kaynak adreslerine dayalı yeni bir kural ekle:

`sudo ip {{[ru|rule]}} {{[a|add]}} from {{192.168.178.2/32}}`

- Paket hedef adreslerine dayalı yeni bir kural ekle:

`sudo ip {{[ru|rule]}} {{[a|add]}} to {{192.168.178.2/32}}`

- Paket kaynak adreslerine dayalı bir kuralı sil:

`sudo ip {{[ru|rule]}} {{[d|delete]}} from {{192.168.178.2/32}}`

- Paket hedef adreslerine dayalı bir kuralı sil:

`sudo ip {{[ru|rule]}} {{[d|delete]}} to {{192.168.178.2/32}}`

- Silinen tüm kuralları temizle:

`sudo ip {{[ru|rule]}} {{[f|flush]}}`

- Tüm kuralları bir dosyaya kaydet:

`ip {{[ru|rule]}} {{[s|save]}} > {{ip_kuralları.dat/dosyasının/yolu}}`

- Tüm kuralları bir dosyadan geri yükle:

`sudo ip {{[ru|rule]}} {{[r|restore]}} < {{ip_kuralları.dat/dosyasının/yolu}}`
