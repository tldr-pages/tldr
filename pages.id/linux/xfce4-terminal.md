# xfce4-terminal

> Emulator terminal XFCE4.
> Informasi lebih lanjut: <https://docs.xfce.org/apps/xfce4-terminal/start>.

- Membuka jendela terminal baru:

`xfce4-terminal`

- Mengatur judul awal:

`xfce4-terminal --initial-title "{{judul_awal}}"`

- Membuka tab baru di jendela terminal saat ini:

`xfce4-terminal --tab`

- Menjalankan sebuah perintah di jendela terminal baru:

`xfce4-terminal --command "{{perintah_dengan_argumen}}"`

- Tetap buka terminal setelah perintah yang dijalankan selesai:

`xfce4-terminal --command "{{perintah_dengan_argumen}}" --hold`

- Membuka beberapa tab baru dan menjalankan perintah di masing-masing tab:

`xfce4-terminal --tab --command "{{perintah_a}}" --tab --command "{{perintah_b}}"`
