# aws s3 cp

> Copia arquivos locais ou objetos do S3 para outros diretórios locais ou no S3.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html>.

- Copia um arquivo local para um bucket específico:

`aws s3 cp {{caminho/do/arquivo}} s3://{{nome_do_bucket}}/{{caminho/para/o/arquivo_remoto}}`

- Copia um objeto específico para outro bucket dentro do S3:

`aws s3 cp s3://{{nome_do_bucket1}}/{{caminho/do/arquivo}} s3://{{nome_do_bucket2}}/{{caminho/para/o/destino}}`

- Copia um objeto específico do S3 para outro bucket mantendo seu nome original:

`aws s3 cp s3://{{nome_do_bucket1}}/{{caminho/do/arquivo}} s3://{{nome_do_bucket2}}`

- Copia objetos do S3 para um diretório local recursivamente:

`aws s3 cp s3://{{nome_do_bucket}} . --recursive`

- Exibe a ajuda:

`aws s3 cp help`
