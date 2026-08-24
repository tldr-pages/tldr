# xfce4-terminal

> Emulator terminal XFCE4.
> Informasi lebih lanjut: <https://docs.xfce.org/apps/xfce4-terminal/start>.

- Buka jendela terminal baru:

`xfce4-terminal`

- Atur judul awal:

`xfce4-terminal --initial-title "{{judul_awal}}"`

- Buka tab baru di jendela terminal saat ini:

`xfce4-terminal --tab`

- Jalankan sebuah perintah di jendela terminal baru:

`xfce4-terminal --command "{{perintah_dengan_argumen}}"`

- Tetap buka terminal setelah perintah yang dijalankan selesai:

`xfce4-terminal --command "{{perintah_dengan_argumen}}" --hold`

- Buka beberapa tab baru dan menjalankan perintah di masing-masing tab:

`xfce4-terminal --tab --command "{{perintah1}}" --tab --command "{{perintah2}}"`
