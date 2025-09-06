# code

> Pengolah kode komputer yang tersedia lintas platform dan dapat diperluas.
> Informasi lebih lanjut: <https://code.visualstudio.com/docs/configure/command-line>.

- Jalankan aplikasi Visual Studio Code:

`code`

- Buka kumpulan berkas atau direktori ke dalam program pengolah:

`code {{jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...}}`

- Bandingkan isi antara dua berkas teks:

`code {{[-d|--diff]}} {{jalan/menuju/berkas1}} {{jalan/menuju/berkas2}}`

- Buka kumpulan berkas atau direktori menuju sebuah jendela pengolah baru:

`code {{[-n|--new-window]}} {{jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...}}`

- Pasang/bongkat suatu paket ekstensi:

`code --{{install|uninstall}}-extension {{penerbit.ekstensi}}`

- Tampilkan daftar ekstensi yang terpasang:

`code --list-extensions`

- Tampilkan daftar ekstensi terpasang beserta versi masing-masing ekstensi:

`code --list-extensions --show-versions`

- Jalankan program pengolah sebagai superuser (root) dengan menyimpan data aplikasi ke dalam suatu direktori:

`sudo code --user-data-dir {{jalan/menuju/direktori}}`
