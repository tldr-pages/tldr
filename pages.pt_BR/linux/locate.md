# locate

> Encontre nomes de arquivos rapidamente.
> Mais informações: <https://manned.org/locate>.

- Procura por padrões no banco de dados. Nota: o banco de dados é recalculado periodicamente (geralmente semanalmente ou diariamente):

`locate {{padrão}}`

- Procura um arquivo pelo seu nome de arquivo exato(um padrão que não contém caracteres curingas é interpretado como `*pattern*`):

`locate */{{nome_do_arquivo}}`

- Recalcula o banco de dados. Você precisa fazer se você quiser achar os arquivos recentementes adicionados:

`sudo updatedb`
