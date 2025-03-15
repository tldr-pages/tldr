# vim

> Vim (Vi IMproved), suatu aplikasi pengolah teks berbasis baris perintah, yang menyediakan beberapa mode untuk berbagai jenis proses manipulasi teks.
> Menekan `<i>` dalam mode normal akan memasuki mode penyisipan (insert). Menekan `<Esc>` akan kembali ke mode normal, yang memungkinkan penggunaan perintah Vim.
> Lihat juga: `vimdiff`, `vimtutor`, `nvim`.
> Informasi lebih lanjut: <https://www.vim.org>.

- Buka suatu berkas:

`vim {{jalan/menuju/berkas}}`

- Buka suatu berkas pada nomor baris teks tertentu:

`vim +{{nomor_baris}} {{jalan/menuju/berkas}}`

- Lihat manual bantuan untuk Vim:

`<:>help<Enter>`

- Simpan dan keluar dari sesi pengolahan teks saat ini:

`{{<Esc><Z><Z>|<Esc><:>x<Enter>|<Esc><:>wq<Enter>}}`

- Masuk ke mode normal dan batalkan operasi terakhir:

`<Esc><u>`

- Cari pola dalam berkas (tekan `<n>`/`<N>` untuk menuju ke kecocokan berikutnya/sebelumnya):

`</>{{pola_pencarian}}<Enter>`

- Lakukan substitusi ekspresi reguler di seluruh berkas:

`<:>%s/{{ekspresi_reguler}}/{{teks_pengganti}}/g<Enter>`

- Tampilkan nomor baris:

`<:>set nu<Enter>`
