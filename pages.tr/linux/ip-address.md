# ip address

> IP adresi yönetimi alt komutu.
> Daha fazla bilgi için: <https://manned.org/ip-address>.

- Ağ arayüzlerini ve ilişkili IP adreslerini listele:

`ip {{[a|address]}}`

- Yalnızca etkin ağ arayüzlerini gösterecek şekilde filtrele:

`ip {{[a|address]}} {{[s|show]}} up`

- Belirli bir ağ arayüzü hakkındaki bilgileri görüntüle:

`ip {{[a|address]}} {{[s|show]}} {{eth0}}`

- Bir ağ arayüzüne bir IP adresi ekle:

`sudo ip {{[a|address]}} {{[a|add]}} {{ip_adresi}} dev {{eth0}}`

- Bir ağ arayüzünden bir IP adresini kaldır:

`sudo ip {{[a|address]}} {{[d|delete]}} {{ip_adresi}} dev {{eth0}}`

- Belirli bir kapsamdaki tüm IP adreslerini bir ağ arayüzünden sil:

`sudo ip {{[a|address]}} {{[f|flush]}} {{eth0}} scope {{global|host|link}}`
