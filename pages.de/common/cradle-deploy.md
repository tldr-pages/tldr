# cradle deploy

> Verwalte Cradle Implementierungen.
> Weitere Informationen: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#deploy>.

- Implementiere Cradle auf einem Server:

`cradle deploy production`

- Implementiere statische Anlagen zu Amazon S3:

`cradle deploy s3`

- Implementiere statische Anlagen inklusive den Yarn Komponenten:

`cradle deploy s3 --include-yarn`

- Implementiere statische Anlagen inklusive dem "upload" Verzeichnis:

`cradle deploy s3 --include-upload`
