# sshpass

> Penyedia kata sandi untuk SSH.
> Cara kerjanya adalah dengan membuat TTY, memasukkan kata sandi ke dalam TTY, lalu mengalihkan (redirect) `stdin` ke sesi SSH.
> Informasi lebih lanjut: <https://manned.org/sshpass>.

- Terhubung ke server jarak jauh (remote host) menggunakan kata sandi yang diberikan pada sebuah deskriptor berkas (dalam kasus ini, `stdin`):

`sshpass -d {{0}} ssh {{pengguna}}@{{nama_host}}`

- Terhubung ke server jarak jauh (remote host) dengan kata sandi yang diberikan sebagai sebuah opsi, dan secara otomatis menerima kunci SSH yang tidak dikenal:

`sshpass -p {{kata_sandi}} ssh -o StrictHostKeyChecking=no {{pengguna}}@{{nama_host}}`

- Terhubung ke server jarak jauh (remote host) menggunakan baris pertama dari sebuah berkas/fail sebagai kata sandi, kemudian secara otomatis menerima kunci SSH yang tidak dikenal, dan jalankan sebuah perintah:

`sshpass -f {{lokasi/ke/berkas}} ssh -o StrictHostKeyChecking=no {{pengguna}}@{{nama_host}} "{{perintah}}"`
