# git

> Sistem kontrol versi terdistribusi.
> Beberapa subperintah seperti `commit`, `add`, `branch`, `checkout`, `push`, dsb. mempunyai dokumentasi terpisah.
> Informasi lebih lanjut: <https://git-scm.com/docs/git>.

- Buat suatu repositori Git baru:

`git init`

- Salin suatu repositori Git jarak jauh dari internet:

`git clone {{https://example.com/repo.git}}`

- Lihat status repositori lokal saat ini:

`git status`

- Tambahkan seluruh perubahan berkas dan direktori untuk membuat komit baru:

`git add {{[-A|--all]}}`

- Lakukan komit terhadap riwayat versi repositori:

`git commit {{[-m|--message]}} {{pesan_komit}}`

- Teruskan komit-komit lokal menuju suatu repositori jarak jauh:

`git push`

- Tarik perubahan-perubahan baru dari suatu repositori jarak jauh:

`git pull`

- Setel ulang seluruh isi repositori lokal menuju versi komit terakhir:

`git reset --hard; git clean {{[-f|--force]}}`
