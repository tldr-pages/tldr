# fc

> Abre o último comando executado em um editor de texto.
> Mais informações: <https://www.gnu.org/software/bash/manual/bash.html#index-fc>.

- Abre o último comando executado no editor de texto padrão do sistema:

`fc`

- Especifica o editor de texto que será utilizado ao executar o comando:

`fc -e {{'emacs'}}`

- Exibe um histórico dos últimos comandos executados:

`fc -l`

- Lista os comandos recentes em ordem reversa:

`fc -l -r`

- Edita e executa um comando do histórico:

`fc {{número}}`

- Edita comandos em um dado intervalo e executa-os:

`fc '{{416}}' '{{420}}'`

- Mosta ajuda:

`fc --help`
