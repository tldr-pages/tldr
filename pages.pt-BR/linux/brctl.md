# brctl

> Administração de pontes de rede.

- Exibir uma lista com informações das pontes de rede existentes:

`sudo brctl show`

- Cria uma ponte de rede:

`sudo brctl add {{nome_da_ponte}}`

- Remover uma ponte de rede:

`sudo brctl del {{nome_da_ponte}}`

- Adicionar uma interface de rede em uma ponte de rede existente:

`sudo brctl addif {{nome_da_ponte}} {{nome_da_interface_de_rede}}`

- Remover uma interface de rede de uma ponte de rede existente:

`sudo brctl delif {{nome_da_ponte}} {{nome_da_interface_de_rede}}`
