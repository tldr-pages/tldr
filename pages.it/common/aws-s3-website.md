# aws s3 website

> Imposta la configurazione del sito web per un bucket.
> Vedi anche: `aws s3`.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/s3/website.html>.

- Configura un bucket come sito web statico:

`aws s3 website {{s3://nome-bucket}} --index-document {{index.html}}`

- Configura una pagina di errore per il sito web:

`aws s3 website {{s3://nome-bucket}} --index-document {{index.html}} --error-document {{error.html}}`
