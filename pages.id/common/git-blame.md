# git blame

> Tampilkan informasi kode hash dan pelaku komit terakhir pada setiap baris dalam suatu file teks.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-blame>.

- Tampilkan file teks beserta informasi nama pelaku dan kode hash komit terakhir pada akhir setiap baris teks:

`git blame {{jalan/menuju/file}}`

- Tampilkan file dengan informasi komit menggunakan alamat surel/[e]mail daripada nama pelaku:

`git blame -e {{jalan/menuju/file}}`

- Tampilkan informasi nama pelaku dan kode hash komit terakhir pada file yang disimpan dalam komit tertentu:

`git blame {{komit}} {{jalan/menuju/file}}`

- Tampilkan informasi nama pelaku dan kode hash komit terakhir pada file yang disimpan sebelum komit tertentu:

`git blame {{komit}}~ {{jalan/menuju/file}}`
