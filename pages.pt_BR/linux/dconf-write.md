# dconf write

> Escreve valores de chave nos bancos de dados dconf.
> Veja também: `dconf`.
> Mais informações: <https://manned.org/dconf>.

- Escreve um valor de chave específico:

`dconf write {{/caminho/para/chave}} "{{valor}}"`

- Escreve uma string específica como valor de chave:

`dconf write {{/caminho/para/chave}} "'{{string}}'"`

- Escreve um inteiro específico como valor de chave:

`dconf write {{/caminho/para/chave}} "{{5}}"`

- Escreve um booleano específico como valor de chave:

`dconf write {{/caminho/para/chave}} "{{true|false}}"`

- Escreve um array específico como valor de chave:

`dconf write {{/caminho/para/chave}} "[{{'primeiro', 'segundo', ...}}]"`

- Escreve um array vazio específico como valor de chave:

`dconf write {{/caminho/para/chave}} "@as []"`
