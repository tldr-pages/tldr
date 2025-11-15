# ip link

> Ağ arayüzlerini yönet.
> Daha fazla bilgi için: <https://manned.org/ip-link>.

- Tüm ağ arayüzleriyle ilgili bilgileri göster:

`ip {{[l|link]}}`

- Belirli bir ağ arayüzüyle ilgili bilgileri göster:

`ip {{[l|link]}} {{[sh|show]}} {{ethN}}`

- Bir ağ arayüzünü etkinleştir veya devre dışı bırak:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethN}} {{up|down}}`

- Bir ağ arayüzüne anlamlı bir ad ver:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethN}} {{[al|alias]}} "{{LAN Arayüzü}}"`

- Bir ağ arayüzünün MAC adresini değiştir:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethN}} {{[a|address]}} {{ff:ff:ff:ff:ff:ff}}`

- Jumbo çerçeveleri kullanması için bir ağ arayüzünün MTU boyutunu değiştir:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethN}} mtu {{9000}}`
