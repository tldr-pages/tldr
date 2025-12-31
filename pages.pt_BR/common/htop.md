# htop

> Exibe informação dinâmica em tempo real acerca de processos em execução. Uma versão melhorada do comando `top`.
> Mais informações: <https://manned.org/htop>.

- Inicializa `htop`:

`htop`

- Inicializa `htop` mostrando somente processos pertencentes a um usuário:

`htop {{[-u|--user]}} {{nome_usuário}}`

- Apresenta os processos de forma hierárquica em uma visão de árvore para mostrar relações de pai-filho:

`htop {{[-t|--tree]}}`

- Ordena processos por um `item_de_ordenação` (utilize `htop --sort help` para ver as opções disponíveis):

`htop {{[-s|--sort]}} {{item_de_ordenação}}`

- Inicializa `htop` com um atraso especificado entre atualizações, em décimos de segundo (p. ex. 50 = 5 segundos):

`htop {{[-d|--delay]}} {{50}}`

- Vê comandos interativos enquanto roda htop:

`<?>`

- Muda para uma aba diferente:

`<Tab>`

- Mostra ajuda:

`htop {{[-h|--help]}}`
