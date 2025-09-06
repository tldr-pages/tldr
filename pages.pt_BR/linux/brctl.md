# brctl

> Administração de pontes de rede.
> Mais informações: <https://manned.org/brctl>.

- Exibe uma lista com informações das pontes de rede existentes:

`sudo brctl show`

- Cria uma ponte de rede:

`sudo brctl add {{nome_da_ponte}}`

- Remove uma ponte de rede:

`sudo brctl del {{nome_da_ponte}}`

- Adiciona uma interface de rede em uma ponte de rede existente:

`sudo brctl addif {{nome_da_ponte}} {{nome_da_interface_de_rede}}`

- Remove uma interface de rede de uma ponte de rede existente:

`sudo brctl delif {{nome_da_ponte}} {{nome_da_interface_de_rede}}`
