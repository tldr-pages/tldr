# gzip

> Ferramenta de compactação de arquivos com compressão gzip.
> Mais informações: <https://www.gnu.org/software/gzip/>.

- Alterar compressão de um arquivo compactado com compressão gzip:

`gzip {{arquivo.ext}}`

- Descompactar arquivo gzip definindo arquivo final:

`gzip -c -d {{arquivo.ext}}.gz > {{arquivo_descompactado.ext}}`

- Compactar arquivo definindo arquivo final:

`gzip -c {{arquivo.ext}} > {{arquivo_compactado.ext.gz}}`

- Compactando arquivos em gzip definindo o nível de compressão [9]:

`gzip -{{9}} -c {{arquivo.ext}} > {{arquivo_compactado.ext.gz}}`
