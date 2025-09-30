# fdisk

> Gerencia de tabelas de partições e partições em um disco rígido.
> Veja também: `partprobe`.
> Mais informações: <https://manned.org/fdisk>.

- Lista partições:

`sudo fdisk -l`

- Inicia o manipulador de partições:

`sudo fdisk {{/dev/sdX}}`

- Uma vez particionando um disco, cria uma partição:

`<n>`

- Uma vez particionando um disco, seleciona uma partição para excluir:

`<d>`

- Uma vez particionando um disco, mostra uma tabela de partições:

`<p>`

- Uma vez particionando um disco, grava em disco as mudanças feitas:

`<w>`

- Uma vez particionando um disco, descarta as mudanças feitas:

`<q>`

- Uma vez particionando um disco, abre o menu de ajuda:

`<m>`
