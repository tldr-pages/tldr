# echo

> Imprime os argumentos passados.
> Mais informações: <https://www.gnu.org/software/coreutils/echo>.

- Imprime uma mensagem de texto. Nota: aspas são opcionais:

`echo "{{Olá Mundo}}"`

- Imprime uma mensagem com variáveis de ambiente:

`echo "{{Meu caminho é $PATH}}"`

- Imprime uma mensagem sem adicionar uma nova linha no final:

`echo -n "{{Olá Mundo}}"`

- Adiciona uma mensagem no arquivo:

`echo "{{Olá Mundo}}" >> {{arquivo.txt}}`

- Habilita interpretação dos códigos de escape após barra invertida (caracteres especiais):

`echo -e "{{Coluna 1\tColuna 2}}"`

- Imprime o status de saída do último comando executado (Nota: no prompt de comando do Windows e no PowerShell, os comandos equivalentes são `echo %errorlevel%` e `$lastexitcode` respectivamente):

`echo $?`
