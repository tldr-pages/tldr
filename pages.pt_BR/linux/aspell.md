# aspell

> Verificador ortográfico interativo.
> Mais informações: <http://aspell.net/>.

- Verificar a ortografia do texto de um arquivo:

`aspell check {{arquivo}}`

- Exibir as palavras escritas incorretamente no terminal:

`cat {{arquivo}} | aspell list`

- Exibir os dicionários disponíveis:

`aspell dicts`

- Executar `aspell` utilizando uma língua diferente (informe o código ISO 639 da língua):

`aspell --lang={{cs}}`

- Exibir os erros ortográficos no terminal e ignorando as palavras da lista pessoal:

`cat {{arquivo}} | aspell --personal={{lista_pessoal.pws}} list`
