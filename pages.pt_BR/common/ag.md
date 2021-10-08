# ag

> The Silver Searcher. Parecido com o ack, mas com um foco em ser ainda mais rápido.
> Mais informações: <https://github.com/ggreer/the_silver_searcher>.

- Achar arquivos que contém "foo" e imprimir as linhas correspondentes no contexto:

`ag {{foo}}`

- Achar arquivos que contém "foo" em um diretório específico:

`ag {{foo}} {{caminho/para/o/arquivo}}`

- Achar arquivos que contém "foo", mas listar somente os nomes dos arquivos:

`ag -l {{foo}}`

- Achar arquivos que contém "FOO" sem diferença de caixa e imprimir somente o correspondente em vez de a linha inteira:

`ag -i -o {{FOO}}`

- Achar "foo" em arquivos cujo nome corresponde a "bar":

`ag {{foo}} -G {{bar}}`

- Achar arquivos cujo conteúdo corresponde à expressão regular:

`ag '{{^ba(r|z)$}}'`

- Achar arquivos cujo nome corresponde a "foo":

`ag -g {{foo}}`
