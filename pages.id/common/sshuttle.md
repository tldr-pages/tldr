# sshuttle

> Server proksi transparan yang meneruskan lalu lintas (traffic) melalui koneksi SSH.
> Tidak memerlukan root atau pengaturan khusus di server SSH jarak jauh, namun akses root di mesin lokal akan diminta.
> Informasi lebih lanjut: <https://manned.org/sshuttle>.

- Teruskan semua lalu lintas TCP IPv4 melalui server SSH jarak jauh:

`sshuttle {{[-r|--remote]}} {{nama_pengguna}}@{{server_ssh}} {{0.0.0.0/0}}`

- Teruskan juga semua lalu lintas DNS ke DNS resolver default milik server:

`sshuttle --dns {{[-r|--remote]}} {{nama_pengguna}}@{{server_ssh}} {{0.0.0.0/0}}`

- Teruskan semua lalu lintas kecuali yang ditujukan untuk subnet tertentu:

`sshuttle {{[-r|--remote]}} {{nama_pengguna}}@{{server_ssh}} {{0.0.0.0/0}} {{[-x|--exclude]}} {{192.168.0.1/24}}`

- Gunakan metode tproxy untuk meneruskan semua lalu lintas IPv4 dan IPv6:

`sshuttle --method tproxy {{[-r|--remote]}} {{nama_pengguna}}@{{server_ssh}} {{0.0.0.0/0}} {{::/0}} {{[-x|--exclude]}} {{alamat_ip_lokal_anda}} {{[-x|--exclude]}} {{alamat_ip_server_ssh}}`
