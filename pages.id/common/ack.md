# ack

> Sebuah alat pencari teks seperti `grep` yang dikhususkan bagi para pengembang perangkat lunak.
> Lihat juga: `rg`, yang dapat mencari dengan lebih cepat.
> Informasi lebih lanjut: <https://beyondgrep.com/documentation>.

- Cari file dalam direktori saat ini yang mengandung string atau kriteria dalam ekspresi reguler:

`ack "{{pola_pencarian}}"`

- Cari tanpa mementingkan perbedaan huruf besar-kecil dalam kriteria (case-insensitive):

`ack --ignore-case "{{pola_pencarian}}"`

- Cari untuk baris-baris dalam file yang memenuhi kriteria, namun hanya cetak teks yang memenuhinya saja (jangan cetak kata-kata lainnya meskipun dalam baris yang sama):

`ack -o "{{pola_pencarian}}"`

- Hanya cari file dengan tipe tertentu (seperti `ruby` untuk mencari file `.rb`,`.erb`, `.rake`, `Rakefile` dan sebagainya):

`ack --type {{ruby}} "{{pola_pencarian}}"`

- Jangan cari file dengan tipe tertentu:

`ack --type no{{ruby}} "{{pola_pencarian}}"`

- Hitung total teks/string yang ditemukan:

`ack --count --no-filename "{{pola_pencarian}}"`

- Hanya cetak nama file dan total penemuan dalam file tersebut saja:

`ack --count --files-with-matches "{{pola_pencarian}}"`

- Tampilkan daftar kombinasi nilai yang dapat dipakai dalam atribut `--type`:

`ack --help-types`
