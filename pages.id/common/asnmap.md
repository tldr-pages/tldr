# asnmap

> Suatu alat baris perintah berbasis Go untuk memetakan rentang jaringan organisasi beserta kepemilikannya menggunakan data ASN.
> Catatan: Membutuhkan sebuah kunci API dari layanan ProjectDiscovery Cloud Platform.
> Informasi lebih lanjut: <https://github.com/projectdiscovery/asnmap#usage>.

- Cari rentang CIDR untuk suatu ASN:

`asnmap {{[-a|-asn]}} {{AS5650}} -silent`

- Cari rentang CIDR untuk suatu alamat IP:

`asnmap {{[-i|-ip]}} {{100.19.12.21}} -silent`

- Cari rentang CIDR untuk suatu nama domain:

`asnmap {{[-d|-domain]}} {{example.com}} -silent`

- Cari rentang CIDR untuk suatu nama organisasi:

`asnmap -org {{GOOGLE}} -silent`

- Cari rentang CIDR berdasarkan daftar target pencarian dalam suatu berkas:

`asnmap {{[-f|-file]}} {{jalan/menuju/target.txt}} -silent`

- Keluarkan hasil dalam format JSON:

`asnmap {{[-d|-domain]}} {{facebook.com}} {{[-j|-json]}} -silent`

- Keluarkan hasil dalam format CSV:

`asnmap {{[-a|-asn]}} {{AS394161}} {{[-c|-csv]}} -silent`

- Perbarui asnmap menuju versi terkini:

`asnmap {{[-up|-update]}}`
