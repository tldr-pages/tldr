# winget

> Manajer Paket Antarmuka Baris Perintah Windows.
> Informasi lebih lanjut: <https://learn.microsoft.com/windows/package-manager/winget>.

- Pasang suatu paket:

`winget install {{nama_paket}}`

- Hapus paket yang terpasang sebelumnya (Catatan: subperintah `uninstall` juga dapat digantikan dengan `remove`):

`winget uninstall {{nama_paket}}`

- Tampilkan informasi tentang paket:

`winget show {{nama_paket}}`

- Cari paket:

`winget search {{nama_paket}}`

- Perbarui seluruh paket menuju versi terkini:

`winget upgrade --all`

- Tampilkan paket terpasang yang dapat dikelola oleh `winget`:

`winget list --source winget`

- Impor atau ekspor daftar paket terpasang ke dalam suatu file:

`winget {{import|export}} {{--import-file|--output}} {{jalan/menuju/berkas}}`

- Lakukan uji validasi manifes pemaketan winget sebelum mengirimkan rencana perubahan (Pull Request) menuju repositori winget-pkgs:

`winget validate {{jalan/menuju/manifes}}`
