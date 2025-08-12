# pw-link

> Gerenciar conexões entre portas no PipeWire.
> Mais informações: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- Lista todos as saídas e entradas de áudio com seus IDs:

`pw-link {{[-oiI|--output --input --id]}}`

- Cria uma conexão entre uma porta de entrada e uma porta de saída:

`pw-link {{output_port_name}} {{input_port_name}}`

- Desconecta duas portas:

`pw-link {{[-d|--disconnect]}} {{output_port_name}} {{input_port_name}}`

- Lista todas as conexões com seus IDs:

`pw-link {{[-lI|--links --id]}}`

- Exibe ajuda:

`pw-link {{[-h|--help]}}`
