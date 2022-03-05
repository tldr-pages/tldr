# nmcli device

> NetworkManager ile donanım aygıtı yönetimi.
> Daha fazla bilgi: <https://man.archlinux.org/man/nmcli.1>.

- Tüm ağ arayüzlerinin durumlarını yazdır:

`nmcli device status`

- Kullanılabilir kablosuz erişim noktalarını yazdır:

`nmcli device wifi`

- Belirtilen ad ve parola ile kablosuz ağa bağlan:

`nmcli device wifi connect {{ssid}} password {{parola}}`

- Geçerli kablosuz ağ için parola ve QR kodunu yazdır:

`nmcli device wifi show-password`
