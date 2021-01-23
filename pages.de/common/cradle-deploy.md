# cradle deploy

> Management von Cradle Deployments.
> Mehr Informationen: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#deploy>.

- Deployment von Cradle auf einen Server:

`cradle deploy production`

- Deployment statischer Anlagen zu Amazon S3:

`cradle deploy s3`

- Deployment statischer Anlagen inklusive der Yarn Komponenten:

`cradle deploy s3 --include-yarn`

- Deployment statischer Anlagen inklusive des "upload" Verzeichnisses:

`cradle deploy s3 --include-upload`
