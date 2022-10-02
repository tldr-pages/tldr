# certutil

> Gerencie chaves e certificados em bancos de dados e tokens NSS
> Mais informações: <https://manpages.ubuntu.com/manpages/xenial/man1/certutil.1.html>.

- Criar um novo banco de dados de certificados:

`certutil -N -d .`

- Listar todos os certificados em um banco de dados:

`certutil -L -d .`

- Listar todas as chaves privadas em um banco de dados:

`certutil -K -d . -f pwdfile.txt`

- Importar o certificado assinado para o banco de dados dos solicitantes:

`certutil -A -n "Server-cert" -t ",," -i server.crt -d .`

- Para adicionar nomes de assunto alternativos, use uma list separada por vírgulas com a opção -8 IE:

`certutil -S -f pwdfile.txt -d . -t ",," -c "Server-Cert" -n "server1" -g 2048 -s "CN=testuser1,O=testrelm.test"`
