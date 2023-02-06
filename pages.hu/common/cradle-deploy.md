# cradle deploy

> Cradle telepítések kezelése. További információ: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#deploy>.

- A Cradle telepítése egy kiszolgálóra:

`cradle deploy production`

- Statikus eszközök telepítése az Amazon S3-ra:

`cradle deploy s3`

- Statikus eszközök telepítése, beleértve a Yarn "components" könyvtárat:

`cradle deploy s3 --include-yarn`

- Statikus eszközök telepítése a "upload" könyvtárat is beleértve:

`cradle deploy s3 --include-upload`
