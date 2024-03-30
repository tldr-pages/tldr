# git blame

> Tampilkan informasi kode hash dan pelaku komit terakhir pada setiap baris dalam suatu berkas teks.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-blame>.

- Tampilkan berkas teks beserta informasi nama pelaku dan kode hash komit terakhir pada akhir setiap baris teks:

`git blame {{jalan/menuju/berkas}}`

- Tampilkan berkas dengan informasi komit menggunakan alamat surel/[e]mail daripada nama pelaku:

`git blame -e {{jalan/menuju/berkas}}`

- Tampilkan informasi nama pelaku dan kode hash komit terakhir pada berkas yang disimpan dalam komit tertentu:

`git blame {{komit}} {{jalan/menuju/berkas}}`

- Tampilkan informasi nama pelaku dan kode hash komit terakhir pada berkas yang disimpan sebelum komit tertentu:

`git blame {{komit}}~ {{jalan/menuju/berkas}}`
