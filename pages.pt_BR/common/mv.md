# mv

> Movimentação de arquivos entre diretórios, ou renomeá-los.
> Mais informações: <https://www.gnu.org/software/coreutils/mv>.

- Move um arquivo para um diretório arbitrário:

`mv {{percorso/del/arquivo}} {{percorso/del/destino}}`

- Move arquivos para outro diretório, mantendo os nomes dos arquivos:

`mv {{percorso/del/arquivo_1 percorso/del/arquivo_2 ...}} {{percorso/del/destino}}`

- Não requisita confirmação para sobrescrição de arquivos:

`mv -f {{percorso/del/arquivo}} {{percorso/del/destino}}`

- Requisita confirmação para sobrescrição de arquivos, independentemente das permissões de arquivo:

`mv -i {{percorso/del/arquivo}} {{percorso/del/destino}}`

- Não sobrescrita arquivos existentes no diretório de destino:

`mv -n {{percorso/del/arquivo}} {{percorso/del/destino}}`

- Move os arquivos em modo Verbose, mostrando os arquivos após sua movimentação:

`mv -v {{percorso/del/arquivo}} {{percorso/del/destino}}`
