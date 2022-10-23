# rubocop

> Menganalisa file Ruby.
> Informasi lebih lanjut: <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- Memeriksa semua file dalam direktori saat ini (termasuk direktori-direktori di dalamnya):

`rubocop`

- Memeriksa satu atau lebih file atau direktori secara khusus:

`rubocop {{lokasi/ke/file}} {{lokasi/ke/direktori}}`

- Menulis output ke file:

`rubocop --out {{lokasi/ke/file}}`

- Melihat daftar _cop_ (aturan-aturan dalam analisis):

`rubocop --show-cops`

- Mengecualikan _cop_:

`rubocop --except {{cop_1}} {{cop_2}}`

- Menjalankan hanya beberapa _cop_:

`rubocop --only {{cop_1}} {{cop_2}}`

- Memperbaiki file secara otomatis (fitur percobaan):

`rubocop --auto-correct`
