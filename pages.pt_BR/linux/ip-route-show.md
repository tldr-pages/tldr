# ip route show

> Exibe subcomando para o gerenciamento de tabelas de roteamento de IP.
> Mais informações: <https://manned.org/ip-route>.

- Exibe a tabela de roteamento:

`ip {{[r|route]}} show`

- Exibe a tabela de roteamento principal (mesmo que o primeiro exemplo):

`ip {{[r|route]}} show {{main|254}}`

- Exibe a tabela de roteamento local:

`ip {{[r|route]}} show table {{local|255}}`

- Exibe todas as tabelas de roteamento:

`ip {{[r|route]}} show table {{all|unspec|0}}`

- Lista rotas apenas a partir de um dispositivo provido:

`ip {{[r|route]}} show dev {{eth0}}`

- Lista rotas dentro de um escopo provido:

`ip {{[r|route]}} show scope link`

- Exibe o cache de roteamento:

`ip {{[r|route]}} show cache`

- Exibe apenas rotas IPv6 ou IPv4:

`ip {{-6|-4}} {{[r|route]}} show`
