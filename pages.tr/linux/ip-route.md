# ip route

> IP yönlendirme tablosu yönetimi alt komutu.
> Daha fazla bilgi için: <https://manned.org/ip-route>.

- Yönlendirme tablosunu görüntüle:

`ip {{[r|route]}}`

- Ağ geçidini kullanan öntanımlı bir yönlendirme ekle:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{ağ_geçidi_ip_adresi}}`

- `eth0` arayüzünü kullanan öntanımlı bir yönlendirme ekle:

`sudo ip {{[r|route]}} {{[a|add]}} default dev {{eth0}}`

- Statik bir yönlendirme ekle:

`sudo ip {{[r|route]}} {{[a|add]}} {{hedef_ip_adresi}} via {{ağ_geçidi_ip_adresi}} dev {{eth0}}`

- Statik bir yönlendirmeyi sil:

`sudo ip {{[r|route]}} {{[d|delete]}} {{hedef_ip_adresi}} dev {{eth0}}`

- Statik bir yönlendirmeyi değiştir:

`sudo ip {{[r|route]}} {{change|replace}} {{hedef_ip_adresi}} via {{ağ_geçidi_ip_adresi}} dev {{eth0}}`

- Bir IP adresine ulaşmak için çekirdek tarafından hangi yönlendirmenin kullanılacağını göster:

`ip {{[r|route]}} {{[g|get]}} {{hedef_ip_adresi}}`
