# command

> Obriga o shell a executar o programa, ignorando qualquer função ou alias com o mesmo nome.
> Mais informações: <https://www.gnu.org/software/bash/manual/bash.html#index-command>.

- Executa o programa ls, mesmo que exista algum alias ls:

`command {{ls}}`

- Exibe o caminho para o executável ou a definição do apelido de um comando específico:

`command -v {{command_name}}`
