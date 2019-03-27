# brctl

> Administração de bridge ethernet.

- Exibe uma lista com informações sobre as ethernet bridges existentes:

`sudo brctl show`

- Cria uma ethernet bridge:

`sudo brctl add {{bridge_name}}`

- Remove uma ethernet bridge:

`sudo brctl del {{bridge_name}}`

- Adiciona uma interface de rede a uma ethernet bridge existente:

`sudo brctl addif {{bridge_name}} {{interface_name}}`

- Remove uma interface de rede a uma ethernet bridge existente:

`sudo brctl delif {{bridge_name}} {{interface_name}}`
