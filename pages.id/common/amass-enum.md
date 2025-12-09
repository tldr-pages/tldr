# amass enum

> Cari seluruh subdomain dari suatu domain internet.
> Informasi lebih lanjut: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Cari para subdomain dari suatu [d]omain (secara pasif):

`amass enum -d {{nama_domain}}`

- Cari para subdomain dari [d]omain dengan memeriksa apakah subdomain tersebut dapat ditemukan:

`amass enum -active -d {{nama_domain}} -p {{80,443,8080}}`

- Lakukan pencarian terhadap para sub[d]omain secara paksa (brute force):

`amass enum -brute -d {{nama_domain}}`

- Simpan hasil pencarian ke dalam suatu berkas teks:

`amass enum -o {{berkas_output}} -d {{nama_domain}}`

- Simpan hasil luaran (output) terminal menuju suatu berkas dan informasi tambahan ke dalam direktori tertentu:

`amass enum -o {{berkas_output}} -dir {{jalan/menuju/direktori}} -d {{nama_domain}}`

- Tampilkan daftar sumber pencarian data:

`amass enum -list`
