# cradle deploy

> Gestisci distribuzioni Cradle.

- Distribuisci Cradle su un server:

`cradle deploy production`

- Distribuisci assets statici ad Amazon S3:

`cradle deploy s3`

- Distribuisci assets statici, inclusa la directory "components" di Yarn:

`cradle deploy s3 --include-yarn`

- Distribuisci assets statici, includendo la directory "upload":

`cradle deploy s3 --include-upload`
