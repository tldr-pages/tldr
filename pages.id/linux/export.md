# export

> Ekspor variabel menuju anak-anak proses syel sistem operasi.
> Informasi lebih lanjut: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- Setel nilai suatu variabel lingkungan syel (environment variable):

`export {{VARIABEL}}={{nilai}}`

- Hapus nilai variabel lingkungan:

`export -n {{VARIABEL}}`

- Ekspor suatu fungsi perintah (function) menuju anak-anak proses syel:

`export -f {{NAMA_FUNGSI}}`

- Tambahkan alamat direktori baru menuju variabel lingkungan `PATH`:

`export PATH=$PATH:{{path/to/append}}`

- Tampilkan daftar variabel yang telah diekspor dalam bentuk kode perintah syel:

`export -p`
