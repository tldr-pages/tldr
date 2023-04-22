# genisoimage

> Genisoimage é um programa de pré-masterização usado para gerar sistemas de arquivos híbridos ISO9660/Joliet/HFS.
> Mais informações: <https://manpages.debian.org/latest/genisoimage/genisoimage.1.en.html>.

- Criar uma imagem ISO a partir do diretório de origem fornecido:

`genisoimage -o {{minhaimagem.iso}} {{caminho/para/diretório_origem}`

- Criar uma imagem ISO com arquivos maiores que 2GiB a partir do diretório de origem fornecido:

`genisoimage -o -allow-limited-size {{minhaimagem.iso}} {{caminho/para/diretório_origem}}`
