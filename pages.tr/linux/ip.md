# ip

> Yönlendirmeyi, aygıtları, kural yönlendirmesini ve tünelleri görüntüle / değiştir.
> `address` gibi bazı alt komutların kendi kullanım belgeleri vardır.
> Daha fazla bilgi için: <https://manned.org/ip.8>.

- Arayüzlerin bilgilerini ayrıntılı bir şekilde listele:

`ip {{[a|address]}}`

- Arayüzlerin ağ katmanı bilgilerini kısa bir şekilde listele:

`ip {{[-br a|-brief address]}}`

- Arayüzlerin bağlantı katmanı bilgilerini kısa bir şekilde listele:

`ip {{[-br l|-brief link]}}`

- Yönlendirme tablosunu görüntüle:

`ip {{[r|route]}}`

- Komşuları (ARP tablosunu) göster:

`ip {{[n|neighbour]}}`

- Bir arayüzü etkinleştir/devre dışı bırak:

`sudo ip {{[l|link]}} {{[s|set]}} {{arayüz}} {{up|down}}`

- Bir arayüze IP adresi ekle/sil:

`sudo ip {{[a|address]}} {{add|delete}} {{ip}}/{{maske}} dev {{arayüz}}`

- Öntanımlı yönlendirme ekle:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{ip}} dev {{arayüz}}`
