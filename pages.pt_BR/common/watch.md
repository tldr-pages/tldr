# watch

> Execute um programa periodicamente e monitore a saída no modo de tela cheia.
> Mais informações: <https://manned.org/watch>.

- Executar repetidamente um comando e mostrar o resultado:

`watch {{comando}}`

- Executar novamente um comando a cada 60 segundos:

`watch {{[-n|--interval]}} 60 {{comando}}`

- Monitore o espaço em disco, destacando as diferenças à medida que elas aparecem:

`watch {{[-d|--differences]}} {{df}}`

- Executar repetidamente um pipeline e mostrar o resultado:

`watch "{{comando_1}} | {{comando_2}} | {{comando_3}}"`

- Saia do `watch` se a saída visível for alterada:

`watch {{[-g|--chgexit]}} {{lsblk}}`

- Interpretar caracteres de controle do terminal:

`watch {{[-c|--color]}} {{ls --color=always}}`
