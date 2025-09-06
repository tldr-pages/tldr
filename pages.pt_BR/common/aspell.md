# aspell

> Verificador ortográfico interativo.
> Mais informações: <http://aspell.net/>.

- Verifica a ortografia do texto de um arquivo:

`aspell check {{arquivo}}`

- Exibe as palavras escritas incorretamente no terminal:

`cat {{arquivo}} | aspell list`

- Exibe os dicionários disponíveis:

`aspell dicts`

- Executa `aspell` utilizando uma língua diferente (informe o código ISO 639 da língua):

`aspell --lang={{cs}}`

- Exibe os erros ortográficos no terminal e ignorando as palavras da lista pessoal:

`cat {{arquivo}} | aspell --personal={{lista_pessoal.pws}} list`
