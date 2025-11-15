# diff

> Bandingkan isi berkas dan direktori.
> Informasi lebih lanjut: <https://manned.org/diff>.

- Bandingkan isi berkas-berkas (tampilkan daftar isi yang diubah dari `berkas_lawas` sehingga membentuk `berkas_baru`):

`diff {{berkas_lawas}} {{berkas_baru}}`

- Bandingkan isi berkas-berkas, tanpa menghiraukan karakter spasi:

`diff {{[-w|--ignore-all-space]}} {{berkas_lawas}} {{berkas_baru}}`

- Bandingkan isi berkas-berkas, dan tampilkan perbedaannya secara samping-men[y]amping:

`diff {{[-y|--side-by-side]}} {{berkas_lawas}} {{berkas_baru}}`

- Bandingkan isi berkas-berkas, dan tampilkan perbedaannya dalam format menyatu (sebagaimana digunakan dalam `git diff`):

`diff {{[-u|--unified]}} {{berkas_lawas}} {{berkas_baru}}`

- Bandingkan direktori-direktori secara rekursif (tampilkan nama-nama berkas/direktori beserta segala perubahan atas isi berkas-berkas):

`diff {{[-r|--recursive]}} {{direktori_lawas}} {{direktori_baru}}`

- Bandingkan direktori-direktori, dan hanya tampilkan nama berkas yang berbeda isi:

`diff {{[-r|--recursive]}} {{[-q|--brief]}} {{direktori_lawas}} {{direktori_baru}}`

- Buat suatu berkas patch untuk Git dari perbedaan atas kedua berkas teks, dengan memperlakukan berkas yang tidak tersedia sebagai kosong:

`diff {{[-a|--text]}} {{[-u|--unified]}} {{[-N|--new-file]}} {{berkas_lawas}} {{berkas_baru}} > {{diff.patch}}`

- Bandingkan berkas-berkas, menampilkan luaran program secara berwarna dan upayakan untuk mencari perubahan-perubahan secara minimal:

`diff {{[-d|--minimal]}} --color=always {{berkas_lawas}} {{berkas_baru}}`
