# find

> Procura recursivamente por arquivos ou diretórios em uma árvore de diretórios.
> Veja também: `fd`.
> Mais informações: <https://manned.org/find>.

- Procura por arquivos pela extensão:

`find {{caminho/para/diretorio}} -name '{{*.ext}}'`

- Procura por arquivos que correspondam a vários padrões específicos de caminho/nome:

`find {{caminho/para/diretorio}} -path '{{**/caminho/**/*.ext}}' -or -name '{{*nome*}}'`

- Procura por diretórios que correspondam a um nome específico, sem diferenciar maiúsculo de minúsculo:

`find {{caminho/para/diretorio}} -type d -iname '{{*nome*}}'`

- Procura por arquivos que correspondam a um nome específico, excluindo certos caminhos:

`find {{caminho/para/diretorio}} -name '{{*.py}}' -not -path '{{*/caminho/*}}'`

- Procura por arquivos que correspondam a uma faixa de tamanho específica, limitando a profundidade recursiva para "1":

`find {{caminho/para/diretorio}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- Executa um comando para cada arquivo (use `{}` dentro do comando para acessar o nome do arquivo):

`find {{caminho/para/diretorio}} -name '{{*.ext}}' -exec {{wc -l}} {} \;`

- Procura por todos os arquivos modificados hoje e passa os resultados para um único comando como argumentos:

`find {{caminho/para/diretorio}} -daystart -mtime {{-1}} -exec {{tar -cvf arquivo.tar}} {} \+`

- Procura por arquivos vazios (0 byte) ou diretórios e os exclui de forma verbosa:

`find {{caminho/para/diretorio}} -type {{f|d}} -empty -delete -print`
