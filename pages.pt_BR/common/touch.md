# touch

> Atualizar as timestamps de um arquivo para a hora atual.
> Se o arquivo não existir, cria um arquivo vazio, a menos que seja passado o parâmetro -c ou -h.
> Mais informações: <https://www.gnu.org/software/coreutils/touch>.

- Criar um novo arquivo vazio, ou atualizar as timestamps para a hora atual:

`touch {{arquivo}}`

- Definir as timestamps de um arquivo para a hora especificada:

`touch -t {{YYYYMMDDHHMM.SS}} {{arquivo}}`

- Usar as timestamps do arquivo1 para definir as timestamps do arquivo2:

`touch -r {{arquivo1}} {{arquivo2}}`

- Alterar as timestamps de um arquivo. Não cria novo arquivo se não existir:

`touch -c {{arquivo}}`
