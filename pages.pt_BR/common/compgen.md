# compgen

> Um programa para auto completar comandos no Bash, ele é executado ao pressionar duas vezes a tecla TAB.
> Mais informações: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- Exibir todos os comandos que você pode executar:

`compgen -c`

- Exibir todos os alias:

`compgen -a`

- Exibir todas as funções que você pode executar:

`compgen -A function`

- Exibir todas as palavras reservadas do shell:

`compgen -k`

- Exibir todos os comandos/alias que iniciam com o termo 'ls':

`compgen -ac {{ls}}`
