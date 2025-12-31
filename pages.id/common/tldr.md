# tldr

> Tampilkan laman bantuan sederhana untuk alat baris perintah (command-line) dari proyek dokumentasi tldr-pages.
> Catatan: opsi `--language` dan `--list` sering diimplementasikan oleh program-program klien meskipun tak diwajibkan menurut spesifikasi teknis.
> Informasi lebih lanjut: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Tampilkan laman bantuan sederhana untuk suatu perintah (catatan: beginilah cara Anda sampai di sini!):

`tldr {{perintah}}`

- Tampilkan laman bantuan sederhana untuk suatu subperintah:

`tldr {{perintah}} {{subperintah}}`

- Tampilkan laman bantuan untuk suatu perintah dalam suatu bahasa (jika tersedia, selainnya dalam bahasa Inggris):

`tldr {{[-L|--language]}} {{kode_bahasa}} {{perintah}}`

- Tampilkan laman bantuan untuk suatu perintah pada [p]latform tujuan:

`tldr {{[-p|--platform]}} {{android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows}} {{command}}`

- M[u]takhirkan data cache lokal untuk laman-laman bantuan:

`tldr {{[-u|--update]}}`

- Tampilkan daftar seluruh laman bantuan untuk perintah-perintah yang tersedia pada platform saat ini dan `common` (lintas platform):

`tldr {{[-l|--list]}}`

- Tampilkan daftar seluruh laman bantuan subperintah yang tersedia untuk dokumentasi suatu perintah induk:

`tldr {{[-l|--list]}} | grep {{perintah}} | column`

- Tampilkan suatu laman bantuan untuk perintah yang dipilih secara acak:

`tldr {{[-l|--list]}} | shuf {{[-n|--head-count]}} 1 | xargs tldr`
