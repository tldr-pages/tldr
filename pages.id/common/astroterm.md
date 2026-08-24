# astroterm

> Sebuah peta bintang untuk terminal.
> Informasi lebih lanjut: <https://github.com/da-luce/astroterm#usage>.

- Tampilkan posisi kumpulan bintang dan planet secara langsung berdasarkan lokasi Anda saat ini:

`astroterm`

- Tampilkan kumpulan konstelasi secara berwarna-warni dan dengan kecepatan bingkai animasi tertentu:

`astroterm {{[-C|--constellations]}} {{[-c|--color]}} {{[-f|--fps]}} {{60}}`

- Gunakan karakter unicode daripada ASCII dasar dan hanya tampilkan kumpulan bintang yang lebih terang dari nilai yang diberikan:

`astroterm {{[-u|--unicode]}} {{[-t|--threshold]}} {{2.0}}`

- Gunakan lintang, bujur, dan tanggal/waktu yang diberikan:

`astroterm {{[-a|--latitude]}} {{90.0}} {{[-o|--longitude]}} {{-180.0}} {{[-d|--datetime]}} {{2025-08-04T12:00:00}}`

- Gunakan garis bujur dan garis lintang kota yang diberikan dan atur kecepatan simulasi ke faktor tertentu:

`astroterm {{[-i|--city]}} {{Singapore}} {{[-s|--speed]}} {{1000.0}}`
