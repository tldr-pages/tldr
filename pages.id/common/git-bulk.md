# git bulk

> Lakukan operasi yang sama dalam lebih dari satu repositori Git.
> Bagian dari `git-extras`.
> Informasi lebih lanjut: <https://github.com/tj/git-extras/blob/master/Commands.md#git-bulk>.

- Daftarkan direktori saat ini sebagai tempat kerja (workspace):

`git bulk --addcurrent {{nama_workspace}}`

- Masukkan tempat kerja saat ini ke dalam daftar direktori yang akan diubah:

`git bulk --addworkspace {{nama_workspace}} {{/jalan/absolut/menuju/repositori}}`

- Gandakan sebuah repositori ke dalam direktori induk tertentu, kemudian masukkan repositori baru tersebut sebagai tempat kerja:

`git bulk --addworkspace {{nama_workspace}} {{/jalan/absolut/menuju/direktori_induk}} --from {{lokasi_repositori_remote}}`

- Gandakan lebih dari satu repositori ke dalam direktori induk tertentu (menurut berkas daftar lokasi remote yang dipisah dengan barisan baru), kemudian masukkan sebagai tempat kerja:

`git bulk --addworkspace {{nama_workspace}} {{/jalan/absolut/menuju/direktori_induk}} --from {/jalan/absolut/menuju/berkas}}`

- Hapus suatu tempat dari daftar tempat kerja (hal ini tidak akan menghilangkan seluruh isi direktori yang direferensikan sebagai tempat kerja):

`git bulk --removeworkspace {{nama_workspace}}`

- Hapus seluruh tempat dari daftar tempat kerja:

`git bulk --purge`
