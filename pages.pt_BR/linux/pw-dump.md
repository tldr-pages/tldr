# pw-dump

> Exibe o estado atual do PipeWire como JSON, incluindo as informações sobre nós, dispositivos, módulos, portas e outros objetos.
> Veja também: `pw-mon`.
> Mais informações: <https://docs.pipewire.org/page_man_pw-dump_1.html>.

- Exibe uma representação em JSON do estado atual da instância padrão do PipeWire:

`pw-dump`

- Exibe o estado atual monitorando mudanças, exibindo-as novamente:

`pw-dump --monitor`

- Salva o estado atual de uma instância remota para um arquivo:

`pw-dump --remote {{nome_do_remoto}} > {{caminho/para/arquivo.json}}`

- Define uma configuração de [C]or:

`pw-dump --color {{never|always|auto}}`

- Exibir ajuda:

`pw-dump --help`
