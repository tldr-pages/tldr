# arp-scan

> Envia pacotes ARP para máquinas (identificadas por endereço IP ou por nomes de domínio) realizarem a varredura da rede local.

- Realizar a varredura da rede local:

`arp-scan --localnet`

- Realizar a varredura baseado no IP da rede com um bitmask customizada:

`arp-scan {{192.168.1.1}}/{{24}}`

- Realizar a varredura baseado em uma faixa de IP em uma rede:

`arp-scan {{127.0.0.0}}-{{127.0.0.31}}`

- Realizar a varredura baseado no IP da rede com uma máscara de rede customizada:

`arp-scan {{10.0.0.0}}:{{255.255.255.0}}`
