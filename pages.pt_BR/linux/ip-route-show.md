# ip route show

> Exibe subcomando para o gerenciamento de tabelas de roteamento de IP.
> Mais informações: <https://manned.org/ip-route>.

- Exibe a tabela de roteamento:

`ip route show`

- Exibe a tabela de roteamento principal (mesmo que o primeiro exemplo):

`ip route show {{main|254}}`

- Exibe a tabela de roteamento local:

`ip route show table {{local|255}}`

- Exibe todas as tabelas de roteamento:

`ip route show table {{all|unspec|0}}`

- Lista rotas apenas a partir de um dispositivo provido:

`ip route show dev {{eth0}}`

- Lista rotas dentro de um escopo provido:

`ip route show scope link`

- Exibe o cache de roteamento:

`ip route show cache`

- Exibe apenas rotas IPv6 ou IPv4:

`ip {{-6|-4}} route show`
