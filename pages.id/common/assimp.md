# assimp

> Klien baris perintah untuk pustaka Open Asset Import Library.
> Mendukung pemuatan 40+ format file 3D, dan mengekspor ke beberapa format 3D populer.
> Informasi lebih lanjut: <https://manned.org/assimp>.

- Tampilkan daftar format berkas impor yang didukung:

`assimp listext`

- Tampilkan daftar format berkas ekspor yang didukung:

`assimp listexport`

- Ubah isi suatu berkas menuju salah satu dari format berkas ekspor/luaran yang didukung, menggunakan daftar parameter bawaan:

`assimp export {{berkas_masukan.stl}} {{berkas_luaran.obj}}`

- Ubah isi suatu berkas menggunakan kumpulan parameter kustom (daftar parameter yang tersedia dapat dilihat pada berkas dox_cmd.h pada kode sumber assimp):

`assimp export {{berkas_masukan.stl}} {{berkas_luaran.obj}} {{kumpulan_parameter}}`

- Tampilkan ringkasan isi suatu berkas objek 3D:

`assimp info {{jalan/menuju/berkas}}`

- Tampilkan bantuan:

`assimp help`

- Tampilkan bantuan atas suatu subperintah:

`assimp {{subperintah}} --help`
