# git authors

> Buat daftar pelaku komit pada suatu repositori Git.
> Bagian dari `git-extras`.
> Informasi lebih lanjut: <https://github.com/tj/git-extras/blob/master/Commands.md#git-authors>.

- Tampilkan daftar pelaku komit menuju `stdout` daripada menuju ke file `AUTHORS`:

`git authors --list`

- Masukkan daftar pelaku komit menuju file `AUTHORS`, kemudian buka file tersebut pada aplikasi penyunting file teks default:

`git authors`

- Masukkan daftar pelaku komit tanpa informasi alamat surel/email menuju file `AUTHORS`, kemudian buka file tersebut pada aplikasi penyunting file teks default:

`git authors --no-email`
