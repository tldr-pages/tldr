# aws s3

> Interface de linha de comando para AWS S3.
> Provê armazenamento através de uma interface de web services.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- Exibe arquivos de um bucket:

`aws s3 ls {{nome_do_bucket}}`

- Sincroniza arquivos e diretórios locais para o bucket:

`aws s3 sync {{caminho/para/arquivos}} s3://{{nome_do_bucket}}`

- Sincroniza arquivos e diretórios do bucket para diretório local:

`aws s3 sync s3://{{nome_do_bucket}} {{caminho/para/diretório}}`

- Sincroniza arquivos e diretórios excluindo algo:

`aws s3 sync {{caminho/para/arquivos}} s3://{{nome_do_bucket}} --exclude {{arquivo/não/sincronizado}} --exclude {{caminho/não/sincronizado}}/*`

- Remove arquivo do bucket:

`aws s3 rm s3://{{nome_do_bucket}}/{{caminho/do/arquivo}}`

- Somente exibe a prévia das mudanças:

`aws s3 {{qualquer_comando}} --dryrun`
