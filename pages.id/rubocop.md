# rubocop

> Menganalisa file Ruby.
> Informasi lebih lanjut: <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- Memeriksa semua file dalam direktori saat ini (termasuk direktori-direktori di dalamnya):

`rubocop`

- Memeriksa satu atau lebih file atau direktori secara khusus:

`rubocop {{jalan/menuju/file}} {{jalan/menuju/direktori}}`

- Menulis output ke file:

`rubocop --out {{jalan/menuju/file}}`

- Melihat daftar cop (aturan-aturan dalam menganalisa):

`rubocop --show-cops`

- Mengecualikan cop:

`rubocop --except {{cop_1}} {{cop_2}}`

- Menjalankan hanya beberapa cop:

`rubocop --only {{cop_1}} {{cop_2}}`

- Memperbaiki file secara otomatis (fitur percobaan):

`rubocop --auto-correct`
