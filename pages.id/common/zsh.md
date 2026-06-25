# zsh

> Z SHell, suatu penerjemah baris perintah yang kompatibel dengan standar bahasa Bash.
> Lihat juga: `bash`, `!`, `^`.
> Informasi lebih lanjut: <https://zsh.sourceforge.io/Doc/Release/Invocation.html#Invocation>.

- Jalankan sesi interaktif baru:

`zsh`

- Jalankan perintah secara spesifik:

`zsh -c "{{echo Halo dunia}}"`

- Jalankan suatu naskah/skrip perintah:

`zsh {{jalan/menuju/naskah.zsh}}`

- Periksa suatu naskah/skrip perintah untuk kesalahan sintaks tanpa menjalankan isi perintahnya:

`zsh {{[-n|--no-exec]}} {{jalan/menuju/naskah.zsh}}`

- Baca dan jalankan kumpulan perintah dari `stdin`:

`{{echo echo Hello world}} | zsh`

- Execute a specific script, printing each command in the script before executing it:

`zsh {{[-x|--xtrace]}} {{jalan/menuju/naskah.zsh}}`

- Jalankan sesi interaktif baru dengan mengeluarkan kembali isi perintah masukan sebelum menjalankannya:

`zsh {{[-v|--verbose]}}`

- Jalankan sesi interaktif baru tanpa memuat perintah konfigurasi awal tingkat pengguna (misalnya dari `~/.zshrc`):

`zsh {{[-f|--no-rcs]}}`
