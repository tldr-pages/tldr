# ag

> The Silver Searcher. Parecido com o ack, mas com um foco em ser ainda mais rápido.
> Mais informações: <https://github.com/ggreer/the_silver_searcher>.

- Acha arquivos que contém "foo" e imprime as linhas correspondentes no contexto:

`ag {{foo}}`

- Acha arquivos que contém "foo" em um diretório específico:

`ag {{foo}} {{caminho/para/arquivo}}`

- Acha arquivos que contém "foo", mas lista somente os nomes dos arquivos:

`ag -l {{foo}}`

- Acha arquivos que contém "FOO" sem diferença de caixa e imprime somente o correspondente em vez de a linha inteira:

`ag -i -o {{FOO}}`

- Acha "foo" em arquivos cujo nome corresponde a "bar":

`ag {{foo}} -G {{bar}}`

- Acha arquivos cujo conteúdo corresponde à expressão regular:

`ag '{{^ba(r|z)$}}'`

- Acha arquivos cujo nome corresponde a "foo":

`ag -g {{foo}}`
