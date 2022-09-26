# nvm

> Memasang, melepas, atau mengganti versi Node.js yang dipakai.
> Mendukung nomor versi seperti "12.8" or "v16.13.1", dan label versi seperti "stable", "system", dsb.
> Informasi lebih lanjut: <https://github.com/creationix/nvm>.

- Memasang versi Node.js yang ditentukan:

`nvm install {{versi_node_js}}`

- Menggunakan versi Node.js tertentu untuk sesi saat ini:

`nvm use {{versi_node_js}}`

- Menyetel versi Node.js secara default:

`nvm alias default {{versi_node_js}}`

- Menunjukkan daftar versi Node.js yang tersedia dan versi Node.js yang disetel sebagai default:

`nvm list`

- Menghapus sebuah versi Node.js yang terpasang melalui `nvm`:

`nvm uninstall {{versi_node_js}}`

- Menjalankan interpreter (REPL) Node.js dengan versi tertentu:

`nvm run {{versi_node_js}} --version`

- Menjalankan sebuah file atau aplikasi JavaScript di dalam Node.js versi tertentu:

`nvm exec {{versi_node_js}} node {{app.js}}`
