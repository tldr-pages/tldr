# apt-mark

> Alat untuk mengubah status pemasangan kumpulan paket.
> Informasi lebih lanjut: <https://manned.org/apt-mark>.

- Tandai suatu paket sebagai "terpasang secara otomatis" (misalnya, sebagai bagian ketergantungan / dependensi dari paket lain):

`sudo apt-mark auto {{nama_paket}}`

- Tahan suatu paket agar tidak diubah atau diperbarui ke dalam versi lainnya:

`sudo apt-mark hold {{nama_paket}}`

- Lepaskan penahanan suatu paket agar dapat diperbarui kembali:

`sudo apt-mark unhold {{nama_paket}}`

- Tampilkan daftar paket yang terpasang secara manual:

`apt-mark showmanual`

- Tampilkan daftar paket yang ditahan dari pembaruan peranti lunak:

`apt-mark showhold`
