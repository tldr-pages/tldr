# tldr

> Tampilkan laman bantuan sederhana untuk alat baris perintah (command-line) dari proyek dokumentasi tldr-pages.
> Catatan: Opsi `--language` dan `--list` sering diimplementasikan oleh program-program klien meskipun tak diwajibkan menurut spesifikasi teknis.
> Informasi lebih lanjut: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Tampilkan laman bantuan sederhana untuk suatu perintah (catatan: beginilah cara Anda sampai di sini!):

`tldr {{perintah}}`

- Tampilkan laman bantuan sederhana untuk suatu subperintah:

`tldr {{perintah}} {{subperintah}}`

- Tampilkan laman bantuan untuk suatu perintah dalam suatu bahasa (jika tersedia, selainnya dalam bahasa Inggris):

`tldr {{[-L|--language]}} {{kode_bahasa}} {{perintah}}`

- Tampilkan laman bantuan untuk suatu perintah pada [p]latform tujuan:

`tldr {{[-p|--platform]}} {{android|cisco-ios|common|dos|freebsd|linux|netbsd|openbsd|osx|sunos|windows}} {{perintah}}`

- M[u]takhirkan data cache lokal untuk laman-laman bantuan:

`tldr {{[-u|--update]}}`

- Tampilkan daftar seluruh laman bantuan untuk perintah-perintah yang tersedia pada platform saat ini dan `common` (lintas platform):

`tldr {{[-l|--list]}}`

- Lihat isi laman tldr dalam jendela terminal (`fzf` harus tersedia terlebih dahulu):

`tldr {{[-l|--list]}} | fzf --preview "tldr {1} --color=always" --preview-window=right,70% | xargs tldr`

- Tampilkan suatu laman bantuan untuk perintah yang dipilih secara acak:

`tldr {{[-l|--list]}} | shuf {{[-n|--head-count]}} 1 | xargs tldr`
