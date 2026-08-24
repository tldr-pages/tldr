# autossh

> Jalankan, awasi, dan hubungkan ulang koneksi-koneksi SSH.
> Menghubungkan koneksi SSH kembali secara otomatis untuk menjaga terowongan penerusan port tetap aktif. Menerima semua argumen standar perintah SSH.
> Informasi lebih lanjut: <https://manned.org/autossh>.

- Jalankan suatu sesi SSH, hubungkan kembali saat port yang diawasi ([M]onitoring) gagal mengembalikan data:

`autossh -M {{port_untuk_diawasi}} "{{perintah_ssh}}"`

- Teruskan suatu port [L]okal menuju port jarak jauh, hubungkan kembali bila diperlukan:

`autossh -M {{port_untuk_diawasi}} -L {{port_lokal}}:localhost:{{port_jarak_jauh}} {{pengguna}}@{{hostname}}`

- Jalankan `autossh` ke dalam proses latar belakang sebelum menjalankan SSH dan jangan ([N]o) membuka sesi shell jarak jauh:

`autossh -f -M {{port_untuk_diawasi}} -N "{{perintah_ssh}}"`

- Jalankan dalam latar belakang, daripada mengawasi port apapun, kirimkan paket SSH keep-alive setiap 10 detik untuk mendeteksi kegagalan koneksi:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{perintah_ssh}}"`

- Jalankan dalam latar belakang, tanpa mengawasi port apapun maupun membuka sesi shell, dan hentikan saat proses penerusan port gagal:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{port_lokal}}:localhost:{{port_jarak_jauh}} {{pengguna}}@{{hostname}}`

- Jalankan dalam latar belakang, dan simpan log awakutu `autossh` dan SSH menuju berkas-berkas tertentu:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{jalan/menuju/berkas_log_autossh.log}} autossh -f -M {{port_untuk_diawasi}} -v -E {{jalan/menuju/berkas_log_ssh.log}} {{perintah_ssh}}`
