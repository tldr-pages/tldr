# cradle deploy

> Gestionați implementările Cradle.
> Mai multe informaţii: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#deploy>

- Implementați Cradle pe un server:

`cradle deploy production`

- Implementați active statice pentru Amazon S3:

`cradle deploy s3`

- Implementați active statice, inclusiv directorul „componente” Yarn:

`cradle deploy s3 --include-yarn`

- Implementarea activelor statice, inclusiv directorul „upload”:

`cradle deploy s3 --include-upload`
