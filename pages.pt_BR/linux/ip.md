# ip

> Mostra / manipula roteamento, dispositivos, roteamento baseado em póliticas e túneis.
> Alguns subcomandos como `address` têm suas pŕoprias documentações de uso.
> Mais informações: <https://manned.org/ip.8>.

- Lista interfaces com informações detalhadas:

`ip {{[a|address]}}`

- Lista interfaces com breves informações sobre a camada de rede:

`ip {{[-br a|-brief address]}}`

- Lista interfaces com breves informações sobre a camada de link de dados:

`ip {{[-br l|-brief link]}}`

- Exibe a tabela de roteamento:

`ip {{[r|route]}}`

- Mostra vizinhos (ARP tabela):

`ip {{[n|neighbour]}}`

- Ativa / desativa uma interface:

`sudo ip {{[l|link]}} {{[s|set]}} {{interface}} {{up|down}}`

- Adiciona / remove um endereço de IP a uma interface:

`sudo ip {{[a|address]}} {{add|delete}} {{ip}}/{{mask}} dev {{interface}}`

- Adiciona uma rota padrão:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{ip}} dev {{interface}}`
