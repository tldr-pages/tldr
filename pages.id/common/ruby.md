# ruby

> Interpreter bahasa pemrograman Ruby.
> Informasi lebih lanjut: <https://manned.org/ruby>.

- Jalankan suatu berkas skrip atau program Ruby:

`ruby {{jalan/menuju/skrip.rb}}`

- Jalankan suatu perintah Ruby dalam command-line:

`ruby -e {{perintah}}`

- Periksa kesalahan sintaks dari suatu berkas skrip Ruby:

`ruby -c {{jalan/menuju/skrip.rb}}`

- Jalankan program peladen (server) HTTP bawaan terrhadap direktori saat ini menuju port 8080:

`ruby -run -e httpd`

- Jalankan suatu berkas biner program Ruby tanpa memasang suatu pustaka (library) pendukung yang diwajibkan:

`ruby -I {{jalan/menuju/direktori_pustaka}} -r {{nama_pustaka_yang_dikecualikan}} {{jalan/menuju/direktori_bin/nama_berkas_bin}}`

- Tampilkan [v]ersi Ruby saat ini:

`ruby {{[-v|--version]}}`
