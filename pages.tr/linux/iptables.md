# iptables

> Linux çekirdek IPv4 güvenlik duvarının; tablolarını, zincirlerini ve kurallarını yapılandırın.
> IPv6 trafiğini ayarlamak için `ip6tables` kullanın.
> Ayrıca bakınız: `iptables-save`, `iptables-restore`.
> Daha fazla bilgi için: <https://manned.org/iptables>.

- Filtre tablosu için zincirleri, kuralları, paket/bayt sayaçlarını ve satır numaralarını görüntüleyin:

`sudo iptables {{[-vnL --line-numbers|--verbose --numeric --list --line-numbers]}}`

- Zincir politikası kuralını ayarlayın:

`sudo iptables {{[-P|--policy]}} {{zincir}} {{kural}}`

- Verilen kuralı belirtilen IP için zincir politikasına uygulayın:

`sudo iptables {{[-A|--append]}} {{zincir}} {{[-s|--source]}} {{ip}} {{[-j|--jump]}} {{kural}}`

- Protokol ve portu dikkate alarak verilen IP için zincir politikasına kural ekle:

`sudo iptables {{[-A|--append]}} {{zincir}} {{[-s|--source]}} {{ip}} {{[-p|--protocol]}} {{tcp|udp|icmp|...}} --dport {{port}} {{[-j|--jump]}} {{kural}}`

- `192.168.0.0/24` alt ağından gelen tüm trafiği ana bilgisayarın açık IP adresine yönlendirmek için bir NAT kuralı ekleyin:

`sudo iptables {{[-t|--table]}} {{nat}} {{[-A|--append]}} {{POSTROUTING}} {{[-s|--source]}} {{192.168.0.0/24}} {{[-j|--jump]}} {{MASQUERADE}}`

- Zincir kuralını silin:

`sudo iptables {{[-D|--delete]}} {{zincir}} {{kural_satır_numarası}}`
