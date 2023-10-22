# certutil

> Gerencie chaves e certificados em bancos de dados e tokens NSS.
> Mais informações: <https://manned.org/certutil>.

- Cria um novo banco de dados de certificados:

`certutil -N -d .`

- Lista todos os certificados em um banco de dados:

`certutil -L -d .`

- Lista todas as chaves privadas em um banco de dados:

`certutil -K -d . -f {{caminho/para/arquivo_de_senha.txt}}`

- Importa o certificado assinado para o banco de dados dos solicitantes:

`certutil -A -n "{{certificado_do_servidor}}" -t ",," -i {{caminho/para/arquivo.crt}} -d .`

- Adiciona nomes de assunto a um determinado certificado:

`certutil -S -f {{caminho/para/arquivo_de_senha.txt}} -d . -t ",," -c "{{certificado_do_servidor}}" -n "{{nome_do_servidor}}" -g {{2048}} -s "CN={{nome_comum}},O={{organização}}"`
