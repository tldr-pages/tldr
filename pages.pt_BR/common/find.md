# find

> Procura recursivamente por arquivos ou diretórios em uma árvore de diretórios.
> Mais informações: <https://manned.org/find>.

- Procura por arquivos pela extensão:

`find {{caminho_raiz}} -name '{{*.ext}}'`

- Procura por arquivos que correspondam a vários padrões específicos de caminho/nome:

`find {{caminho_raiz}} -path '{{**/caminho/**/*.ext}}' -or -name '{{*nome*}}'`

- Procura por diretórios que correspondam a um nome específico, sem diferenciar maiúsculo de minúsculo:

`find {{caminho_raiz}} -type d -iname '{{*nome*}}'`

- Procura por arquivos que correspondam a um nome específico, excluindo certos caminhos:

`find {{caminho_raiz}} -name '{{*.py}}' -not -path '{{*/caminho/*}}'`

- Procura por arquivos que correspondam a uma faixa de tamanho específica, limitando a profundidade recursiva para "1":

`find {{caminho_raiz}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- Executa um comando para cada arquivo (use `{}` dentro do comando para acessar o nome do arquivo):

`find {{caminho_raiz}} -name '{{*.ext}}' -exec {{wc -l}} {} \;`

- Procura por todos os arquivos modificados hoje e passa os resultados para um único comando como argumentos:

`find {{caminho_raiz}} -daystart -mtime {{-1}} -exec {{tar -cvf arquivo.tar}} {} \+`

- Procura por arquivos vazios (0 byte) ou diretórios e os exclui de forma verbosa:

`find {{caminho_raiz}} -type {{f|d}} -empty -delete -print`
