# hdiutil

> Utilitário para criar e gerenciar imagens de disco.
> Mais informações: <https://keith.github.io/xcode-man-pages/hdiutil.1.html>.

- Monta uma imagem:

`hdiutil attach {{caminho/para/aquivo_de_imagem}}`

- Desmonta uma imagem:

`hdiutil detach /Volumes/{{nome_do_volume}}`

- Lista as imagens montadas:

`hdiutil info`

- Cria uma imagem ISO a partir do conteúdo de um diretório:

`hdiutil makehybrid -o {{caminho/para/arquivo_de_saída}} {{caminho/para/diretório}}`
