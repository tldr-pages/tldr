# aplay

> Pemutar suara untuk driver kartu suara ALSA.
> Informasi lebih lanjut: <https://manned.org/aplay>.

- Dengarkan file audio tertentu (sampling rate, bit depth, dll. akan ditentukan secara otomatis berdasarkan format file):

`aplay {{jalan/menuju/berkas}}`

- Dengarkan file audio 10 detik pertama dari file tertentu pada 2500 Hz:

`aplay {{[-d|--duration]}} 10 {{[-r|--rate]}} 2500 {{jalan/menuju/berkas}}`

- Dengarkan file raw sebagai file `.au` dengan 22050 Hz, mono, 8-bit, Mu-Law:

`aplay {{[-c|--channels]}} 1 {{[-t|--file-type]}} raw {{[-r|--rate]}} 22050 {{[-f|--format]}} mu_law {{jalan/menuju/berkas}}`

- Tampilkan daftar perangkat audio yang tersedia:

`aplay {{[-l|--list-devices]}}`
