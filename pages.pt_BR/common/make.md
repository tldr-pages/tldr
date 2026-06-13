# make

> Ferramenta de execução de tarefas para os destinos descritos no Makefile.
> Principalmente utilizada para controlar a compilação de um executável a partir do código-fonte.
> Mais informações: <https://www.gnu.org/software/make/manual/make.html>.

- Executa o primeiro destino especificado no Makefile (geralmente chamado de "all"):

`make`

- Executa um destino específico:

`make {{destino}}`

- Executa um destino específico, executando 4 tarefas simultaneamente em paralelo:

`make {{[-j|--jobs]}} 4 {{destino}}`

- Usa um Makefile específico:

`make {{[-f|--file]}} {{caminho/para/arquivo}}`

- Executa o make a partir de outro diretório:

`make {{[-C|--directory]}} {{caminho/para/diretorio}}`

- Força a execução de um destino, mesmo que os arquivos de origem não tenham sido alterados:

`make {{[-B|--always-make]}} {{destino}}`

- Substitui uma variável definida no Makefile:

`make {{destino}} {{variavel}}={{novo_valor}}`

- Substitui variáveis definidas no Makefile pelo ambiente:

`make {{[-e|--environment-overrides]}} {{destino}}`
