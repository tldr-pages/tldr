# echo

> Imprime os argumentos passados.
> Mais informações: <https://www.gnu.org/software/coreutils/echo>.

- Imrpime uma mensagem de texto. Nota: aspas são opcionais:

`echo "{{Uma mensagem}}"`

- Imprime uma mensagem com as variáveis de ambiente:

`echo "{{Meu path é $PATH}}"`

- Imprime uma mensagem sem adicionar uma nova linha em seguida:

`echo -n "{{Uma mensagem}}"`

- Adiciona uma messagem no arquivo:

`echo "{{Uma mensagem}}" >> {{arquivo.txt}}`

- Habilita interpretação dos códigos de escape após barra invetida (caracteres especiais):

`echo -e "{{Coluna 1\tColuna 2}}"`
