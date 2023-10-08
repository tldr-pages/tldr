# aws s3 rm

> Exclui objetos do S3.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/rm.html>.

- Exclui um objeto específico do S3:

`aws s3 rm s3://{{nome_do_bucket}}/{{caminho/para/arquivo}}`

- Mostra uma visualização prévia da exclusão de um objeto específico do S3, sem deletá-lo (dry-run):

`aws s3 rm s3://{{nome_do_bucket}}/{{caminho/para/arquivo}} --dryrun`

- Exclui um objeto de um ponto de acesso específico do S3:

`aws s3 rm s3://arn:aws:s3:{{região}}:{{id_da_conta}}:{{ponto_de_acesso}}/{{nome_do_ponto_de_acesso}}/{{chave_do_objeto}}`

- Exibe a ajuda::

`aws s3 rm help`
