# echo

> Cetak ulang argumen-argumen yang dimasukkan ke dalam layar perangkat.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>.

- Cetak sebuah pesan teks. Catatan: penggunaan tanda petik bersifat opsional:

`echo "{{Halo Dunia}}"`

- Cetak sebuah pesan bersama suatu variabel lingkungan (environment variable):

`echo "{{Variabel path saya adalah $PATH}}"`

- Cetak sebuah pesan tanpa mencetak baris teks baru (tanpa [n]ewline):

`echo -n "{{Halo Dunia}}"`

- Tambahkan isi pesan ke dalam suatu berkas teks:

`echo "{{Halo Dunia}}" >> {{berkas.txt}}`

- Aktifkan fitur interpretasi penggunaan tanda garis miring terbalik sebagai penanda karakter khusus:

`echo -e "{{Kolom 1\tKolom 2}}"`

- Cetak status keluar dari perintah terakhir yang dieksekusi (Catatan: Dalam Windows Command Prompt dan PowerShell, perintah yang setara adalah `echo %errorlevel%` dan `$lastexitcode`):

`echo $?`
