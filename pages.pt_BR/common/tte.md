# tte

> Um mecanismo, aplicativo e biblioteca de efeitos visuais para o terminal.
> Mais informações: <https://github.com/ChrisBuilds/terminaltexteffects>.

- Aplica um efeito aleatório à saída de um comando:

`{{comando}} | tte --random-effect`

- Aplica um efeito específico à saída de um comando:

`{{ls -la}} | tte {{matrix}}`

- Mostra as opções de um efeito específico:

`tte {{decrypt}} -h`

- Aplica um efeito ao texto de um arquivo:

`tte --input-file {{caminho/para/arquivo}} {{beams}}`

- Imprime scripts de conclusão para o shell:

`tte --print-completion {{bash}}`
