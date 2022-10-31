# ip route

> IP yönlendirme tablosu yönetimi alt komutu.
> Daha fazla bilgi için: <https://manned.org/ip-route>.

- Yönlendirme tablosunu görüntüle:

`ip route {{show|list}}`

- Ağ geçidini kullanan öntanımlı bir yönlendirme ekle:

`sudo ip route add default via {{ağ_geçidi_ip_adresi}}`

- `eth0` arayüzünü kullanan öntanımlı bir yönlendirme ekle:

`sudo ip route add default dev {{eth0}}`

- Statik bir yönlendirme ekle:

`sudo ip route add {{hedef_ip_adresi}} via {{ağ_geçidi_ip_adresi}} dev {{eth0}}`

- Statik bir yönlendirmeyi sil:

`sudo ip route del {{hedef_ip_adresi}} dev {{eth0}}`

- Statik bir yönlendirmeyi değiştir:

`sudo ip route {{change|replace}} {{hedef_ip_adresi}} via {{ağ_geçidi_ip_adresi}} dev {{eth0}}`

- Bir IP adresine ulaşmak için çekirdek tarafından hangi yönlendirmenin kullanılacağını göster:

`ip route get {{hedef_ip_adresi}}`
