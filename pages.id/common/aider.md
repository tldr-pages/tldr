# aider

> Bangun program bersama LLM pilihan Anda.
> Informasi lebih lanjut: <https://github.com/Aider-AI/aider>.

- Buat suatu proyek baru atau lakukan pengerjaan pada basis kode saat ini:

`aider --model {{nama_model}} --api-key {{kunci_api_anda}}`

- Tambahkan fitur atau kasus uji baru menuju berkas-berkas tertentu:

`aider {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Berikan deskripsi keluhan bug dan biarkan `aider` memperbaikinya:

`aider {{jalan/menuju/berkas}} --describe "{{deskripsi_keluhan_bug}}"`

- Lakukan pemfaktoran ulang kode dalam suatu berkas:

`aider {{jalan/menuju/berkas}} --refactor`

- Mutakhirkan dokumentasi kode:

`aider {{jalan/menuju/berkas}} --update-docs`

- Tampilkan informasi bantuan:

`aider --help`
