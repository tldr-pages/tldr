# aws s3 mv

> Move arquivos locais ou objetos S3 para outra localização localmente ou no S3.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/mv.html>.

- Move um arquivo local para um bucket especificado:

`aws s3 mv {{caminho/para/arquivo_local}} s3://{{nome_do_bucket}}/{{caminho/para/arquivo_remoto}}`

- Move um objeto específico do S3 para outro bucket:

`aws s3 mv s3://{{nome_do_bucket1}}/{{caminho/para/arquivo}} s3://{{nome_do_bucket2}}/{{caminho/para/destino}}`

- Move um objeto específico do S3 para outro bucket mantendo o nome original:

`aws s3 mv s3://{{nome_do_bucket1}}/{{caminho/para/arquivo}} s3://{{nome_do_bucket2}}`

- Exibe a ajuda:

`aws s3 mv help`
