# mv

> Movimentação de arquivos entre diretórios, ou renomeá-los.
> Mais informações: <https://www.gnu.org/software/coreutils/mv>.

- Move um arquivo para um diretório arbitrário:

`mv {{arquivo}} {{destino}}`

- Move arquivos para outro diretório, mantendo os nomes dos arquivos:

`mv {{arquivo_1}} {{arquivo_2}} {{arquivo_3}} {{destino}}`

- Não requisitar confirmação para sobrescrição de arquivos:

`mv -f {{arquivo}} {{destino}}`

- Requisita confirmação para sobrescrição de arquivos, independentemente das permissões de arquivo:

`mv -i {{arquivo}} {{destino}}`

- Não sobrescrita arquivos existentes no diretório de destino:

`mv -n {{arquivo}} {{destino}}`

- Move os arquivos em modo Verbose, mostrando os arquivos após sua movimentação:

`mv -v {{arquivo}} {{destino}}`
