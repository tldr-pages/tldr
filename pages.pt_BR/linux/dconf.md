# dconf

> Gerencia banco de dados dconf.
> Veja também: `dconf-read`, `dconf-reset`, `dconf-write`, `gsettings`.
> Mais informações: <https://manned.org/dconf>.

- Imprime um valor de chave específico:

`dconf read {{/caminho/para/chave}}`

- Imprime sub-diretórios e sub-chaves de um caminho específico:

`dconf list {{/caminho/para/diretório/}}`

- Grava um valor de chave específico:

`dconf write {{/caminho/para/chave}} "{{valor}}"`

- Redefine um valor de chave específico:

`dconf reset {{/caminho/para/chave}}`

- Observa alterações em uma chave/diretório específico:

`dconf watch {{/caminho/para/chave|/caminho/para/diretório/}}`

- Despeja um diretório específico no formato de arquivo INI:

`dconf dump {{/caminho/para/diretório/}}`
