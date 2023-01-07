# nmcli connection

> NetworkManager ile bağlantı yönetimi.
> Daha fazla bilgi için: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Tüm NetworkManager bağlantılarını listele (ad, UUID, tür ve aygıtı gösterir):

`nmcli connection`

- UUID belirterek bağlantıyı etkinleştir:

`nmcli connection up uuid {{uuid}}`

- Bağlantıyı devre dışı bırak:

`nmcli connection down uuid {{uuid}}`

- IPv4 ve IPv6 otomatik olarak yapılandırılan bir bağlantı oluştur:

`nmcli connection add ifname {{arayüz_adı}} type {{ethernet}} ipv4.method {{auto}} ipv6.method {{auto}}`

- Statik bir yalnızca IPv6 bağlantısı oluştur:

`nmcli connection add ifname {{arayüz_adı}} type {{ethernet}} ip6 {{2001:db8::2/64}} gw6 {{2001:db8::1}} ipv6.dns {{2001:db8::1}} ipv4.method {{ignore}}`

- Statik bir yalnızca IPv4 bağlantısı oluştur:

`nmcli connection add ifname {{arayüz_adı}} type {{ethernet}} ip4 {{10.0.0.7/8}} gw4 {{10.0.0.1}} ipv4.dns {{10.0.0.1}} ipv6.method {{ignore}}`

- Bir OVPN dosyasından OpenVPN kullanan bir VPN bağlantısı oluştur:

`nmcli connection import type {{openvpn}} file {{vpn_yapılandırması.ovpn/dosyasının/yolu}}`
