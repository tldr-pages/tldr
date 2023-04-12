# genisoimage

> genisoimage é um programa de pré-masterização usado para gerar sistemas de arquivos híbridos ISO9660/Joliet/HFS..
> Mais informações: <https://manpages.debian.org/stretch/genisoimage/genisoimage.1.en.html>.

- Criar uma imagem ISO:

`genisoimage -o {{minhaimagem.iso} {{caminho/para/a/pasta/}}`

- Criar uma imagem ISO com arquivos maiores que 4GB:

`genisoimage -o -allow-limited-size {{minhaimagem.iso} {{caminho/para/a/pasta/}}`
