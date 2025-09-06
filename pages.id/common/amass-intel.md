# amass intel

> Kumpulkan data pendukung pengintaian bersumber terbuka (OSI) terhadap suatu organisasi, seperti domain pangkal dan informasi Nomor Sistem Otonom (ASN).
> Informasi lebih lanjut: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Cari para domain pangkal yang berkaitan dengan rentang alamat ([addr]ess) IP:

`amass intel -addr {{192.168.0.1-254}}`

- Gunakan metode pengintaian secara aktif:

`amass intel -active -addr {{192.168.0.1-254}}`

- Cari para domain pangkal yang berkaitan dengan suatu [d]omain:

`amass intel -whois -d {{nama_domain}}`

- Cari para pihak ASN yang berkaitan dengan suatu [org]anisasi:

`amass intel -org {{nama_organisasi}}`

- Cari daftar domain yang dipegang oleh suatu pihak Nomor Sistem Otonom (ASN) berdasarkan nomornya:

`amass intel -asn {{nomor_asn}}`

- Simpan hasil pencarian ke dalam suatu berkas teks:

`amass intel -o {{berkas_output}} -whois -d {{nama_domain}}`

- Tampilkan daftar sumber pencarian data:

`amass intel -list`
