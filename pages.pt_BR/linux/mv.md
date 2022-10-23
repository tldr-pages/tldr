# mv

> Utilizado para movimentação de arquivos entre diretórios, ou renomeá-los.
> Para mais detalhes, acesse [este site](https://url-to-upstream.tld).

- Para mover arquivos:

`mv <arquivo_1> <arquivo_2> <arquivo_3> <...> <destino>`

*Note que o destino sempre será o último a ser citado, e deverá ser um diretório.*


Exemplo de movimentação:

`mv foto1.png foto2.png foto6.png Palestra`

Também é possível mover todos os arquivos de um diretório para outro, utilizando-se do operador \*.

`mv fotos/* viagem_ao_Rio`

*No exemplo, todas as fotos do diretório "fotos" serão movidas para o diretório "viagem_ao_Rio".*

- Para renomear arquivos:

`mv <arquivo> <novo_nome_do_arquivo>`

Exemplo:

`mv foto1.png abertura_da_palestra.png`
