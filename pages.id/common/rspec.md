# rspec

> Kerangka pengujian kode Ruby berbasis Ruby dan pola pengembangan berbasis kebiasaan (behavior-driven development).
> Informasi lebih lanjut: <https://rspec.info/features/3-13/rspec-core/command-line/>.

- Buat suatu berkas konfigurasi `.rspec` dan berkas pendukung spesifikasi pengujian (spec helper):

`rspec --init`

- Jalankan semua pengujian menurut berkas-berkas spesifikasi:

`rspec`

- Jalankan pengujian menurut berkas-berkas spesifikasi dalam direktori khusus:

`rspec {{jalan/menuju/direktori}}`

- Jalankan beberapa pengujian menurut kumpulan berkas spesifikasi:

`rspec {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Jalankan kasus khusus dalam pengujian menurut berkas-berkas spesifikasi (misalnya tes yang ada di baris 83):

`rspec {{jalan/menuju/berkas}}:{{83}}`

- Jalankan tes dengan seed khusus (untuk pengujian berbasis randomisasi):

`rspec --seed {{angka_seed}}`
