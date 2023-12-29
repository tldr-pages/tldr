# Accelerate

> Sebuah pustaka/library yang memungkinkan kode PyTorch yang sama dapat dijalankan secara menyebar.
> Informasi lebih lanjut: <https://huggingface.co/docs/accelerate/index>.

- Tampilkan informasi lingkungan proyek PyTorch saat ini:

`accelerate env`

- Buat file konfigurasi secara interaktif:

`accelerate config`

- Tampilkan prakiraan kapasitas memori GPU yang dibutuhkan untuk menjalankan model Hugging Face dengan tipe data yang berbeda:

`accelerate estimate-memory {{nama/model}}`

- Uji validitas sebuah file konfigurasi Accelerate:

`accelerate test --config_file {{jalan/menuju/config.yaml}}`

- Jalankan sebuah model PyTorch dengan Accelerate, menggunakan CPU saja:

`accelerate launch {{jalan/menuju/script.py}} {{--cpu}}`

- Jalankan model dengan Accelerate, menggunakan GPU dari 2 perangkat yang berbeda:

`accelerate launch {{jalan/menuju/script.py}} --multi_gpu --num_machines {{2}}`
