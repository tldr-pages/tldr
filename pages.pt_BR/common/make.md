# make

> Ferramenta de execução de tarefas para os destinos descritos no Makefile.
> Principalmente utilizada para controlar a compilação de um executável a partir do código-fonte.
> Mais informações: <https://www.gnu.org/software/make/manual/make.html>.

- Executa o primeiro destino especificado no Makefile (geralmente chamado de "all"):

`make`

- Executa um destino específico:

`make {{destino}}`

- Executa um destino específico, executando 4 tarefas simultaneamente em paralelo:

`make -j{{4}} {{destino}}`

- Usa um Makefile específico:

`make --file {{caminho/para/arquivo}}`

- Execute o make a partir de outro diretório:

`make --directory {{caminho/para/diretorio}}`

- Force a execução de um destino, mesmo que os arquivos de origem não tenham sido alterados:

`make --always-make {{destino}}`

- Substitua uma variável definida no Makefile:

`make {{destino}} {{variavel}}={{novo_valor}}`

- Substitua variáveis definidas no Makefile pelo ambiente:

`make --environment-overrides {{destino}}`
