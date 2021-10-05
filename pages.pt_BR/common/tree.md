# tree

> Exibe o conteúdo do diretório atual em formato de árvore.
> Mais informações: <http://mama.indstate.edu/users/ice/tree/>.

- Exibe os arquivos e diretórios de acordo com o nível de profundidade 'num' informado (onde 1 significa o diretório atual):

`tree -L {{num}}`

- Exibe apenas diretórios:

`tree -d`

- Inclui a exibição de arquivos ocultos com colorização diferenciada:

`tree -a -C`

- Exibe a árvore sem identação, mostrando o caminho completo (usar `-N` para não escapar espaços em branco e caracteres especiais):

`tree -i -f`

- Exibe o tamanho de cada arquivo e o tamanho acumulado de cada diretório, em um formato de leitura para humanos:

`tree -s -h --du`

- Exibe arquivos em uma árvore hierárquica, utilizando um padrão coringa, e eliminando diretórios que não contêm arquivos correspondentes ao informado:

`tree -P '{{*.txt}}' --prune`

- Exibe diretórios em uma árvore hierárquica, utilizando um padrão coringa, e eliminando diretórios que não possuem ancestrais do informado:

`tree -P {{nome_diretorio}} --matchdirs --prune`

- Exibe a árvore ignorando os diretórios informados:

`tree -I '{{nome_diretorio1|nome_diretorio2}}'`
