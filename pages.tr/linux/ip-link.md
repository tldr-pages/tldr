# ip link

> Ağ arayüzlerini yönet.
> Daha fazla bilgi için: <https://manned.org/ip-link>.

- Tüm ağ arayüzleriyle ilgili bilgileri göster:

`ip {{[l|link]}}`

- Belirli bir ağ arayüzüyle ilgili bilgileri göster:

`ip {{[l|link]}} show {{ethN}}`

- Bir ağ arayüzünü etkinleştir veya devre dışı bırak:

`ip {{[l|link]}} set {{ethN}} {{up|down}}`

- Bir ağ arayüzüne anlamlı bir ad ver:

`ip {{[l|link]}} set {{ethN}} alias "{{LAN Arayüzü}}"`

- Bir ağ arayüzünün MAC adresini değiştir:

`ip {{[l|link]}} set {{ethN}} address {{ff:ff:ff:ff:ff:ff}}`

- Jumbo çerçeveleri kullanması için bir ağ arayüzünün MTU boyutunu değiştir:

`ip {{[l|link]}} set {{ethN}} mtu {{9000}}`
