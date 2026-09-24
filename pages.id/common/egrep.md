# egrep

> Cari pola-pola teks tertentu dalam beberapa berkas sekaligus menggunakan pola pencarian `regex` dengan fitur lebih luas.
> Catatan: Perintah ini merupakan alias dari `grep --extended-regexp`.
> Lihat juga: `regex`.
> Informasi lebih lanjut: <https://manned.org/egrep>.

- Cari berkas yang memiliki isi satu atau beberapa karakter:

`egrep '{{a}}+' {{jalan/menuju/berkas}}`

- Cari untuk karakter yang ditemukan sebanyak nol atau satu kali (pemadanan opsional):

`egrep '{{a}}?' {{jalan/menuju/berkas}}`

- Cari untuk pengulangan karakter sebanyak 10 kali secara berurutan:

`egrep '{{a}}{10}' {{jalan/menuju/berkas}}`

- Cari untuk pengulangan karakter sebanyak 3 hingga 7 kali secara berurutan:

`egrep '{{a}}{3,7}' {{jalan/menuju/berkas}}`

- Cari untuk salah satu opsi kata yang dikehendaki:

`egrep '{{kucing}}|{{anjing}}|{{tikus}}' {{jalan/menuju/berkas}}`

- Cari untuk salah satu opsi kata yang dikehendaki di dalam pola pencarian induk:

`egrep 'c({{a}}|{{o}}|{{u}})p' {{jalan/menuju/berkas}}`

- Cari untuk sekelompok karakter yang diulang sebanyak satu atau beberapa kali:

`egrep '({{aeiou}})+' {{jalan/menuju/berkas}}`

- Cari menggunakan penanda standar kelas karakter (informasi lebih lanjut: <https://www.regular-expressions.info/posixbrackets.html>):

`egrep [[{{:alnum:|:alpha:|:space:|...}}]] {{jalan/menuju/berkas}}`
