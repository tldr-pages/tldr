# ip

> Yönlendirmeyi, aygıtları, kural yönlendirmesini ve tünelleri görüntüle / değiştir.
> `ip address` gibi bazı alt komutların kendi kullanım belgeleri vardır.
> Daha fazla bilgi: <https://www.man7.org/linux/man-pages/man8/ip.8.html>.

- Arayüzlerin bilgilerini ayrıntılı bir şekilde listele:

`ip address`

- Arayüzlerin ağ katmanı bilgilerini kısa bir şekilde listele:

`ip -brief address`

- Arayüzlerin bağlantı katmanı bilgilerini kısa bir şekilde listele:

`ip -brief link`

- Yönlendirme tablosunu görüntüle:

`ip route`

- Komşuları (ARP tablosunu) göster:

`ip neighbour`

- Bir arayüzü etkinleştir/devre dışı bırak:

`ip link set {{arayüz}} up/down`

- Bir arayüze IP adresi ekle/sil:

`ip addr add/del {{ip}}/{{maske}} dev {{arayüz}}`

- Öntanımlı yönlendirme ekle:

`ip route add default via {{ip}} dev {{arayüz}}`
