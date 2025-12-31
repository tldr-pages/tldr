# mc

> Minio Client voor objectopslag en bestandssystemen.
> Kan op sommige systemen `mc` of `mcli` heten.
> Meer informatie: <https://minio.github.io/mc/>.

- Voeg verbinding toe aan een S3-server:

`mc alias set {{local}} {{http://localhost:9000}} {{toegangssleutel}} {{privésleutel}}`

- Maak een bucket aan:

`mc mb {{local/bucket_naam}}`

- Toon buckets en hun inhoud recursief:

`mc ls {{local}} --recursive`
