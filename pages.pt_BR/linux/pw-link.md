# pw-link

> Gerenciar conexões entre portas no PipeWire.
> Mais informações: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- Listar todos as saídas e entradas de áudio com seus IDs:

`pw-link --output --input --ids`

- Criar uma conexão entre uma porta de entrada e uma porta de saída:

`pw-link {{output_port_name}} {{input_port_name}}`

- Desconectar duas portas:

`pw-link --disconnect {{output_port_name}} {{input_port_name}}`

- Listar todas as conexões com seus IDs:

`pw-link --links --ids`

- Exibir ajuda:

`pw-link -h`
