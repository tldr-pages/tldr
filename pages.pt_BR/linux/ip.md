# ip

> Mostra / manipula roteamento, dispositivos, roteamento baseado em póliticas e túneis.
> Alguns subcomandos como `ip address` têm suas pŕoprias documentações de uso.
> Mais informação: <https://www.man7.org/linux/man-pages/man8/ip.8.html>.

- Lista interfaces com informações detalhadas:

`ip address`

- Lista interfaces com breves informações sobre a camada de rede:

`ip -brief address`

- Lista interfaces com breves informações sobre a camada de link de dados:

`ip -brief link`

- Exibe a tabela de roteamento:

`ip route`

- Mostra vizinhos (ARP tabela):

`ip neighbour`

- Ativa / desativa uma interface:

`ip link set {{interface}} up/down`

- Adiciona / remove um endereço de IP a uma interface:

`ip addr add/del {{ip}}/{{mask}} dev {{interface}}`

- Adiciona uma rota padrão:

`ip route add default via {{ip}} dev {{interface}}`
