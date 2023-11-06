# duc

> Duc é uma coleção de ferramentas para indexar, inspecionar e visualizar uso do disco. O duc mantém uma base de dados dos tamanhos acumlados dos diretórios do sistema de arquivos, permitindo buscas nessa base, ou a criação de gráficos elegantes.
> Mais informações: <https://duc.zevv.nl/>.

- Indexa o diretório /usr, escrevendo a base de dados para o local default em ~/.duc.db:

`duc index {{/usr}}`

- Lista todos os arquivos e diretórios dentro do /usr/local, mostrando tamanho relativo dos arquivos em um [g]raph (gráfico):

`duc ls -Fg {{/usr/local}}`

- Lista todos os arquivos e diretórios dentro do /usr/local em uma visão de árvore recursiva:

`duc ls -Fg -R {{/usr/local}}`

- Inicia uma interface gráfica para o usuário explorar o sistema de arquivos exibindo o gráfico sunburst:

`duc gui {{/usr}}`

- Executa a interface de console ncurses para explorar o sistema de arquivos:

`duc ui {{/usr}}`

- Exporta as informações da base de dados:

`duc info`
