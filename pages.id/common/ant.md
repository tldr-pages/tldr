# ant

> Apache Ant: bangun dan atur proyek pengembangan piranti lunak berbasis Java.
> Informasi lebih lanjut: <https://ant.apache.org/manual/index.html>.

- Bangun suatu proyek Java dengan pengaturan yang didefinisikan dalam `build.xml` (lokasi default):

`ant`

- Bangun proyek menggunakan berkas/[f]ile pengaturan selain `build.xml`:

`ant -f {{buildfile.xml}}`

- Tampilkan informasi mengenai daftar target pembangunan piranti lunak yang memungkinkan bagi proyek ini:

`ant -p`

- Tampilkan informasi pendukung awakutu ([d]ebugging):

`ant -d`

- Jalankan pembangunan bagi seluruh target pembangunan yang tidak bergantung kepada target-target yang gagal dibangun:

`ant -k`
