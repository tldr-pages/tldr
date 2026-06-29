# fish

> The Friendly Interactive SHell, suatu penerjemah baris perintah yang dirancang secara ramah pengguna.
> Informasi lebih lanjut: <https://fishshell.com/docs/current/cmds/fish.html>.

- Jalankan sesi interaktif baru:

`fish`

- Jalankan sesi interaktif baru tanpa memuat perintah konfigurasi awal:

`fish {{[-N|--no-config]}}`

- Jalankan kumpulan perintah secara spesifik:

`fish {{[-c|--command]}} "{{echo 'fish is executed'}}"`

- Jalankan suatu naskah/skrip perintah:

`fish {{jalan/menuju/naskah.fish}}`

- Check a specific script for syntax errors:

`fish {{[-N|--no-execute]}} {{jalan/menuju/naskah.fish}}`

- Jalankan kumpulan perintah dari `stdin`:

`{{echo "echo 'perintah fish telah dijalankan'"}} | fish`

- Jalankan sesi interaktif baru dalam mode [P]rivat, di mana shell tidak akan mengakses riwayat perintah lama maupun memasukkan riwayat perintah baru:

`fish {{[-P|--private]}}`

- Tentukan dan ekspor nilai-nilai variabel lingkungan yang disimpan untuk setiap perjalanan sesi baru (builtin environment variable):

`set {{[-U|--universal]}} {{[-x|--export]}} {{nama_variabel}} {{nilai_variable}}`
