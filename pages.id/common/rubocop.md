# rubocop

> Analisa berkas Ruby.
> Informasi lebih lanjut: <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- Periksa semua berkas dalam direktori saat ini (termasuk direktori-direktori di dalamnya):

`rubocop`

- Periksa satu atau lebih berkas atau direktori secara khusus:

`rubocop {{jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...}}`

- Tulis output ke berkas:

`rubocop --out {{jalan/menuju/berkas}}`

- Lihat daftar cop (aturan-aturan dalam menganalisa):

`rubocop --show-cops`

- Kecualikan kumpulan cop dalam proses analisa:

`rubocop --except {{cop1 cop2 ...}}`

- Jalankan hanya beberapa cop:

`rubocop --only {{cop1 cop2 ...}}`

- Perbaiki berkas secara otomatis (fitur percobaan):

`rubocop --auto-correct`
