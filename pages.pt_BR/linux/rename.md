# rename

> Renomeia múltiplos arquivos.
> Nota: essa página refere-se ao comando do pacote `util-linux`.
> Para a versão em Perl, veja `file-rename` ou `perl-rename`.
> Aviso: Esse comando não tem nenhuma proteção e sobrescreverá arquivos sem aviso prévio.
> Mais informações: <https://manned.org/rename>.

- Renomeia arquivos usando substituições simples (substitui 'foo' por 'bar' onde quer que se encontre):

`rename {{foo}} {{bar}} {{*}}`

- Dry-run - exibe quais renomeações ocorreriam sem executá-las:

`rename -vn {{foo}} {{bar}} {{*}}`

- Não sobrescreve os arquivos existentes:

`rename -o {{foo}} {{bar}} {{*}}`

- Altera as extensões dos arquivos:

`rename {{.ext}} {{.bak}} {{*.ext}}`

- Acrescenta "foo" no início de todos os nomes de arquivos no diretório atual:

`rename {{''}} {{'foo'}} {{*}}`

- Renomeia um grupo de arquivos com numerações crescente acrescentando zeros aos números até terem 3 dígitos:

`rename {{foo}} {{foo00}} {{foo?}} && rename {{foo}} {{foo0}} {{foo??}}`
