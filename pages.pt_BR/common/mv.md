# mv

> Movimentação de arquivos entre diretórios, ou renomeá-los.
> Mais informações: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>.

- Move um arquivo para um diretório arbitrário:

`mv {{percorso/del/arquivo}} {{percorso/del/destino}}`

- Move arquivos para outro diretório, mantendo os nomes dos arquivos:

`mv {{percorso/del/arquivo_1 percorso/del/arquivo_2 ...}} {{percorso/del/destino}}`

- Não requisita confirmação para sobrescrição de arquivos:

`mv {{[-f|--force]}} {{percorso/del/arquivo}} {{percorso/del/destino}}`

- Requisita confirmação para sobrescrição de arquivos, independentemente das permissões de arquivo:

`mv {{[-i|--interactive]}} {{percorso/del/arquivo}} {{percorso/del/destino}}`

- Não sobrescrita arquivos existentes no diretório de destino:

`mv {{[-n|--no-clobber]}} {{percorso/del/arquivo}} {{percorso/del/destino}}`

- Move os arquivos em modo Verbose, mostrando os arquivos após sua movimentação:

`mv {{[-v|--verbose]}} {{percorso/del/arquivo}} {{percorso/del/destino}}`
