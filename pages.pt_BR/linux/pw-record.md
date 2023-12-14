# pw-record

> Gravar arquivos de áudio através do pipewire.
> Atalho para pw-cat --record.
> Mais informações: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Fazer uma gravação usando o alvo padrão:

`pw-record {{caminho/para/arquivo.wav}}`

- Fazer uma gravação com um volume diferente:

`pw-record --volume={{0.1}} {{caminho/para/arquivo.wav}}`

- Fazer uma gravação usando uma taxa de amostragem diferente:

`pw-record --rate={{6000}} {{caminho/para/arquivo.wav}}`
