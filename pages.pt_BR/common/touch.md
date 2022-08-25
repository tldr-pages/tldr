# touch

> Alterar os timestamps de acesso e de modificação (atime, mtime) de um arquivo.
> Mais informações: <https://www.gnu.org/software/coreutils/touch>.

- Criar novo(s) arquivo(s) vazio(s) ou alterar os timestamps do(s) arquivo(s) para o timestamp atual:

`touch {{caminho/para/arquivo}}`

- Definir os timestamps de um arquivo para uma data e hora específica:

`touch -t {{YYYYMMDDHHMM.SS}} {{caminho/para/arquivo}}`

- Definir os timestamps de um arquivo para uma hora no passado:

`touch -d "{{-1 hour}}" {{caminho/para/arquivo}}`

- Usar as timestamps de um arquivo para definir as timestamps de um segundo arquivo:

`touch -r {{arquivo1}} {{arquivo2}}`

- Criar múltiplos arquivos:

`touch -c {{arquivo{1,2,3}.txt}}`
