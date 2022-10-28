# bat

> Mencetak dan menggabungkan berkas.
> Klon dari `cat` dengan sintaks berwarna dan integrasi Git.
> Informasi lebih lanjut: <https://github.com/sharkdp/bat>.

- Mencetak konten berkas ke keluaran standar:

`bat {{berkas}}`

- Menggabungkan konten beberapa berkas ke berkas tujuan:

`bat {{berkas1}} {{berkas2}} > {{berkas_tujuan}}`

- Menambahkan konten beberapa berkas ke berkas tujuan:

`bat {{berkas1}} {{berkas2}} >> {{berkas_tujuan}}`

- Memberi nomor pada setiap baris keluaran:

`bat -n {{berkas}}`

- Mencetak konten JSON dengan sintaks berwarna:

`bat --language json berkas.json`

- Menampilkan semua bahasa yang didukung:

`bat --list-languages`
