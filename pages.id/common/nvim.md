# nvim

> Neovim, teks editor programmer berbasis Vim, menyediakan beberapa mode untuk manipulasi teks berbeda jenis.
> Tekan `i` masuk mode edit. `<Esc>` kembali ke mode normal, yang tidak mengizinkan penyisipan teks biasa.
> Informasi lebih lanjut: <https://neovim.io>.

- Membuka berkas:

`nvim {{berkas}}`

- Masuk ke mode pengeditan teks (insert mode):

`<Esc>i`

- Menyalin ("yank") atau memotong ("delete") baris saat ini (tempel itu dengan `P`):

`<Esc>{{yy|dd}}`

- Batalkan operasi terakhir:

`<Esc>u`

- Mencari sebuah pattern pada berkas (tekan `n`/`N` untuk pergi ke kecocokan berikutnya/sebelumnya):

`<Esc>/{{pattern_pencarian}}<Enter>`

- Melakukan penggantian regex pada seluruh berkas:

`<Esc>:%s/{{pattern}}/{{pengganti}}/g<Enter>`

- Menyimpan (write) berkas, dan keluar:

`<Esc>:wq<Enter>`

- Keluar tanpa menyimpan:

`<Esc>:q!<Enter>`
