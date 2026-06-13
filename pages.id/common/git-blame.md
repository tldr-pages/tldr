# git blame

> Tampilkan informasi kode hash dan pelaku komit terakhir pada setiap baris dalam suatu berkas teks.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-blame>.

- Tampilkan berkas teks beserta informasi nama pelaku dan kode hash komit terakhir pada akhir setiap baris teks:

`git blame {{jalan/menuju/berkas}}`

- Tampilkan berkas dengan informasi komit menggunakan alamat surel/email daripada nama pelaku:

`git blame {{[-e|--show-email]}} {{jalan/menuju/berkas}}`

- Tampilkan informasi nama pelaku dan kode hash komit terakhir pada berkas yang disimpan dalam komit tertentu:

`git blame {{komit}} {{jalan/menuju/berkas}}`

- Tampilkan informasi nama pelaku dan kode hash komit terakhir pada berkas yang disimpan sebelum komit tertentu:

`git blame {{komit}}~ {{jalan/menuju/berkas}}`

- Tampilkan suatu berkas beserta informasi pelaku komit pada nomor baris teks yang ditentukan:

`git blame -L {{123}} {{jalan/menuju/berkas}}`

- Lakukan anotasi informasi pelaku komit dalam rentang nomor baris teks yang ditentukan:

`git blame -L {{nomor_baris_awal}},{{nomor_baris_akhir}} {{jalan/menuju/berkas}}`

- Lakukan anotasi dalam 10 baris pertama dalam berkas dengan baris pertama memiliki isi teks yang ditentukan:

`git blame -L '/{{isi_teks}}/',+10 {{jalan/menuju/berkas}}`

- Lakukan anotasi dalam suatu berkas tanpa menghiraukan karakter spasi dan pergerakan baris teks:

`git blame -w -C -C -C {{jalan/menuju/berkas}}`
