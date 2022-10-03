# certutil

> Gerencie chaves e certificados em bancos de dados e tokens NSS
> Mais informações: <https://manned.org/certutil>.

- Criar um novo banco de dados de certificados:

`certutil -N -d .`

- Listar todos os certificados em um banco de dados:

`certutil -L -d .`

- Listar todas as chaves privadas em um banco de dados:

`certutil -K -d . -f {{caminho/para/pwdfile.txt}}`

- Importar o certificado assinado para o banco de dados dos solicitantes:

`certutil -A -n "{{Server-cert}}" -t ",," -i {{path/to/file.crt}} -d .`

- Adicionar nomes de assunto a um determinado certificado:

`certutil -S -f {{caminho/para/pwdfile.txt}} -d . -t ",," -c "{{Server-Cert}}" -n "{{server1}}" -g {{2048}} -s "CN={{testuser1}},O={{testrelm.test}}"`
