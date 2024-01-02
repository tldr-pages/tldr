# genisoimage

> Programa de pré-masterização para gerar sistemas de arquivos híbridos ISO9660/Joliet/HFS.
> Mais informações: <https://manpages.debian.org/latest/genisoimage/genisoimage.1.en.html>.

- Cria uma imagem ISO a partir do diretório de origem fornecido:

`genisoimage -o {{minhaimagem.iso}} {{caminho/para/diretório_origem}`

- Cria uma imagem ISO com arquivos maiores que 2GiB, relatando um tamanho aparente menor para o sistema de arquivos ISO9660:

`genisoimage -o -allow-limited-size {{minhaimagem.iso}} {{caminho/para/diretório_origem}}`
