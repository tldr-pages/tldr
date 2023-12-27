# htop

> Exibe informação dinâmica em tempo real acerca de processos em execução. Uma versão melhorada do comando `top`.
> Mais informações: <https://htop.dev/>.

- Inicializa `htop`:

`htop`

- Inicializa `htop` mostrando somente processos pertencentes a um usuário:

`htop --user {{nome_usuário}}`

- Ordena processos por um `item_de_ordenação` (utilize `htop --sort help` para ver as opções disponíveis):

`htop --sort {{item_de_ordenação}}`

- Inicializa `htop` com um atraso especificado entre atualizações, em décimos de segundo (p. ex. 50 = 5 segundos):

`htop --delay {{50}}`

- Vê comandos interativos enquanto roda `htop`:

`?`

- Muda para uma aba diferente:

`tab`

- Mostra ajuda:

`htop --help`
