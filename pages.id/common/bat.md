# bat

> Cetak dan gabungkan berkas.
> Sebuah klon atas program `cat` dengan sintaks berwarna dan integrasi Git.
> Informasi lebih lanjut: <https://github.com/sharkdp/bat>.

- Cetak rapi konten berkas ke `stdout`:

`bat {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Gabungkan konten beberapa berkas ke berkas tujuan:

`bat {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}} > {{jalan/menuju/berkas_tujuan}}`

- Hapus dekorasi dan matikan fitur tampilan halaman (paging) (opsi `--style plain` dapat digantikan dengan `-p`, atau nyalakan kedua opsi dengan `-pp`):

`bat --style plain --pager never {{jalan/menuju/berkas}}`

- Sorot baris tertentu dengan warna latar belakang yang berbeda:

`bat {{[-H|--highlight-line]}} {{10|5:10|:10|10:|10:+5}} {{jalan/menuju/berkas}}`

- Tunjukkan segala karakter yang tak tercetak seperti spasi, tab, atau indikator baris baru:

`bat {{[-A|--show-all]}} {{jalan/menuju/berkas}}`

- Hapus seluruh informasi dekoratif selain nomor baris pada luaran program:

`bat {{[-n|--number]}} {{jalan/menuju/berkas}}`

- Tampilkan sintaks berwarna terhadap berkas JSON dengan mengatur bahasa sintaks berkas secara eksplisit:

`bat {{[-l|--language]}} json {{jalan/menuju/berkas.json}}`

- Tampilka semua jenis bahasa sintaks berkas yang didukung:

`bat {{[-L|--list-languages]}}`
