# nmcli device

> NetworkManager ile donanım aygıtı yönetimi.
> Daha fazla bilgi için: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Tüm ağ arayüzlerinin durumlarını yazdır:

`nmcli device status`

- Kullanılabilir kablosuz erişim noktalarını yazdır:

`nmcli device wifi`

- Belirtilen ad ve parola ile kablosuz ağa bağlan:

`nmcli --ask device wifi connect {{ssid}}`

- Geçerli kablosuz ağ için parola ve QR kodunu yazdır:

`nmcli device wifi show-password`
