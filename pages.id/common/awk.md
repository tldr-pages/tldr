# awk

> Bahasa pemrograman serbaguna yang seringkali digunakan untuk memproses berkas.
> Note: Implementasi AWK yang berbeda (misalnya, gawk, nawk, atau lainnya) akan membuat tautan simbolik dari nama file tertentu ke file biner utama mereka.
> Lihat juga: `gawk`.
> Informasi lebih lanjut: <https://github.com/onetrueawk/awk>.

- Cetak kolom (atau bidang) kelima dalam berkas yang dipisahkan spasi:

`awk '{print $5}' {{lokasi/berkas}}`

- Cetak kolom kedua dari baris yang mengandung "foo" dalam berkas yang dipisahkan spasi:

`awk '/{{foo}}/ {print $2}' {{lokasi/berkas}}`

- Cetak kolom terakhir dari setiap baris dalam sebuah berkas, menggunakan koma (bukan spasi) sebagai pemisah bidang:

`awk -F ',' '{print $NF}' {{lokasi/berkas}}`

- Jumlahkan nilai di kolom pertama dari sebuah berkas dan cetak totalnya:

`awk '{s+=$1} END {print s}' {{lokasi/berkas}}`

- Cetak setiap baris ketiga dimulai dari baris pertama:

`awk 'NR%3==1' {{lokasi/berkas}}`

- Cetak nilai yang berbeda berdasarkan kondisi:

`awk '{if ($1 == "foo") print "Cocok persis foo"; else if ($1 ~ "bar") print "Cocok sebagian bar"; else print "Baz"}' {{lokasi/berkas}}`

- Cetak semua baris yang nilai kolom ke-10nya berada di antara nilai minimum dan maksimum:

`awk '($10 >= {{nilai_min}} && $10 <= {{nilai_maks}})'`

- Cetak tabel pengguna dengan UID >= 1000 beserta header dan output yang terformat, menggunakan titik dua sebagai pemisah (`%-20s` berarti: string 20 karakter rata kiri, `%6s` berarti: string 6 karakter rata kanan):

`awk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Nama", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`
