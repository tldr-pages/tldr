# aws s3 ls

> Lista AWS S3 buckets, pastas (prefixos) e arquivos (objetos).
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/ls.html>.

- Lista todos os buckets:

`aws s3 ls`

- Lista arquivos e pastas na raiz do bucket (`s3://` é opcional):

`aws s3 ls s3://{{nome_do_bucket}}`

- Lista arquivos e pastas diretamente dentro de um diretório:

`aws s3 ls {{nome_do_bucket}}/{{caminho/para/diretório}}/`

- Lista todos os arquivos em um bucket:

`aws s3 ls --recursive {{nome_do_bucket}}`

- Lista todos os arquivos em um path com um dado prefixo:

`aws s3 ls --recursive {{nome_do_bucket}}/{{caminho/para/diretório/}}{{prefixo}}`

- Exibe a ajuda:

`aws s3 ls help`
