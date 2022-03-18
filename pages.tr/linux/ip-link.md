# ip link

> Ağ arayüzlerini yönet.
> Daha fazla bilgi: <https://man7.org/linux/man-pages/man8/ip-link.8.html>.

- Tüm ağ arayüzleriyle ilgili bilgileri göster:

`ip link`

- Belirli bir ağ arayüzüyle ilgili bilgileri göster:

`ip link show {{ethN}}`

- Bir ağ arayüzünü etkinleştir veya devre dışı bırak:

`ip link set {{ethN}} {{up|down}}`

- Bir ağ arayüzüne anlamlı bir ad ver:

`ip link set {{ethN}} alias "{{LAN Arayüzü}}"`

- Bir ağ arayüzünün MAC adresini değiştir:

`ip link set {{ethN}} address {{ff:ff:ff:ff:ff:ff}}`

- Jumbo çerçeveleri kullanması için bir ağ arayüzünün MTU boyutunu değiştir:

`ip link set {{ethN}} mtu {{9000}}`
