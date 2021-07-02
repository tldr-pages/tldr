# arp-scan

> Envia pacotes ARP para máquinas (identificadas por endereço IP ou por nome de domínio) em uma rede local, identificando as máquinas ativas de acordo com as respostas.
> Mais informações: <https://github.com/royhills/arp-scan>.

- Verificar as máquinas da rede local:

`arp-scan --localnet`

- Verificar as máquinas de uma rede IP especificando a máscara de bit:

`arp-scan {{192.168.1.1}}/{{24}}`

- Verificar as máquinas de uma rede IP que estejam em uma faixa de valores:

`arp-scan {{127.0.0.0}}-{{127.0.0.31}}`

- Verificar as máquinas de uma rede IP especificando a máscara de rede:

`arp-scan {{10.0.0.0}}:{{255.255.255.0}}`
