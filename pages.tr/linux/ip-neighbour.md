# ip neighbour

> Komşu/ARP tablosu yönetimi IP alt komutu.
> Daha fazla bilgi için: <https://manned.org/ip-neighbour.8>.

- Komşu/ARP tablosu girdilerini görüntüle:

`ip {{[n|neighbour]}}`

- `eth0` aygıtının komşu tablosundaki girdileri kaldır:

`sudo ip {{[n|neighbour]}} {{[f|flush]}} dev {{eth0}}`

- Bir komşu araması gerçekleştir ve bir komşu girdisi döndür:

`ip {{[n|neighbour]}} {{[g|get]}} {{aranacak_ip}} dev {{eth0}}`

- `eth0` arayüzüne komşu IP adresi için bir ARP girdisi ekle veya sil:

`sudo ip {{[n|neighbour]}} {{add|delete}} {{ip_adresi}} lladdr {{mac_adresi}} dev {{eth0}} nud reachable`

- `eth0` arayüzünde komşu IP adresi için bir ARP girdisini değiştir:

`sudo ip {{[n|neighbour]}} {{change|replace}} {{ip_adresi}} lladdr {{yeni_mac_adresi}} dev {{eth0}}`
