# nvm

> Memasang, lepas, atau ganti versi Node.js yang dipakai.
> Mendukung nomor versi seperti "12.8" or "v16.13.1", dan label versi seperti "stable", "system", dsb.
> Informasi lebih lanjut: <https://github.com/creationix/nvm>.

- Pasang suatu versi Node.js:

`nvm install {{versi_node_js}}`

- Gunakan suatu versi Node.js untuk sesi saat ini:

`nvm use {{versi_node_js}}`

- Tentukan versi default Node.js untuk sesi-sesi berikutnya:

`nvm alias default {{versi_node_js}}`

- Tunjukkan daftar versi Node.js yang tersedia dan yang disetel sebagai default:

`nvm list`

- Hapus pemasangan versi Node.js yang terpasang melalui `nvm`:

`nvm uninstall {{versi_node_js}}`

- Jalankan interpreter (REPL) Node.js dengan versi tertentu:

`nvm run {{versi_node_js}} --version`

- Jalankan suatu berkas atau program JavaScript di dalam Node.js versi tertentu:

`nvm exec {{versi_node_js}} node {{app.js}}`
