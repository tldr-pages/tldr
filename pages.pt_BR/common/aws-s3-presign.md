# aws s3 presign

> Gera uma URL pré-assinada para objetos do Amazon S3.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html>.

- Gera uma URL pré-assinada que é válida por uma hora para um objeto específico do S3:

`aws s3 presign s3://{{nome_do_bucket}}/{{caminho/para/arquivo}}`

- Gera uma URL pré-assinada que é válida por uma duração especificado:

`aws s3 presign s3://{{nome_do_bucket}}/{{caminho/para/arquivo}} --expires-in {{duração_em_segundos}}`

- Exibe a ajuda:

`aws s3 presign help`
