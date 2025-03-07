# ip address

> IP adresi yönetimi alt komutu.
> Daha fazla bilgi için: <https://manned.org/ip-address>.

- Ağ arayüzlerini ve ilişkili IP adreslerini listele:

`ip {{[a|address]}}`

- Yalnızca etkin ağ arayüzlerini gösterecek şekilde filtrele:

`ip {{[a|address]}} show up`

- Belirli bir ağ arayüzü hakkındaki bilgileri görüntüle:

`ip {{[a|address]}} show dev {{eth0}}`

- Bir ağ arayüzüne bir IP adresi ekle:

`ip {{[a|address]}} add {{ip_adresi}} dev {{eth0}}`

- Bir ağ arayüzünden bir IP adresini kaldır:

`ip {{[a|address]}} delete {{ip_adresi}} dev {{eth0}}`

- Belirli bir kapsamdaki tüm IP adreslerini bir ağ arayüzünden sil:

`ip {{[a|address]}} flush dev {{eth0}} scope {{global|host|link}}`
