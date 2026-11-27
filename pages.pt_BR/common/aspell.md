# aspell

> Verificador ortográfico interativo.
> Mais informações: <http://aspell.net/man-html/index.html>.

- Verifica a ortografia do texto de um arquivo:

`aspell check {{caminho/para/arquivo}}`

- Exibe as palavras escritas incorretamente no terminal:

`cat {{caminho/para/arquivo}} | aspell list`

- Exibe os dicionários disponíveis:

`aspell dicts`

- Executa `aspell` utilizando uma língua diferente (informe o código ISO 639 da língua):

`aspell --lang {{cs}}`

- Exibe os erros ortográficos no terminal e ignorando as palavras da lista pessoal:

`cat {{caminho/para/arquivo}} | aspell --personal {{lista_pessoal.pws}} list`
