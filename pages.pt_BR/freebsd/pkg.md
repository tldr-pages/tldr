# pkg

> Gerenciador de pacotes do FreeBSD.
> Mais informações: <https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=8>.

- Instala um novo pacote:

`pkg install {{pacote}}`

- Remove um pacote:

`pkg delete {{pacote}}`

- Atualiza todos os pacotes:

`pkg upgrade`

- Procura um pacote:

`pkg search {{palavra_chave}}`

- Lista os pacotes instalados:

`pkg info`

- Remove dependências desnecessárias:

`pkg autoremove`
