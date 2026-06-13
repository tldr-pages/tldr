# gsettings

> Consulta e modifica configurações do dconf com validação de esquema.
> Mais informações: <https://manned.org/gsettings>.

- Define o valor de uma chave. Falha se a chave não existe ou o valor está fora do intervalo:

`gsettings set {{org.exemplo.esquema}} {{chave-exemplo}} {{valor}}`

- Imprime o valor de uma chave ou o padrão fornecido pelo esquema se a chave não foi definida no `dconf`:

`gsettings get {{org.exemplo.esquema}} {{chave-exemplo}}`

- Desfaz a definição de uma chave, para que o valor padrão do esquema seja usado:

`gsettings reset {{org.exemplo.esquema}} {{chave-exemplo}}`

- Exibe todos os esquemas, chaves e valores (não realocáveis):

`gsettings list-recursively`

- Exibe todas as chaves e valores (padrão se não definido) de um esquema:

`gsettings list-recursively {{org.exemplo.esquema}}`

- Exibe valores permitidos pelo esquema para uma chave (útil com chaves enumeráveis):

`gsettings range {{org.exemplo.esquema}} {{chave-exemplo}}`

- Exibe a descrição legível por humanos de uma chave:

`gsettings describe {{org.exemplo.esquema}} {{chave-exemplo}}`
