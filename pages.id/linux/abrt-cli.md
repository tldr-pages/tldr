# abrt-cli

> Automatic Bug Reporting Tool untuk sistem berbasis Fedora.
> Digunakan untuk mendeteksi, menganalisis, dan melaporkan crash aplikasi.
> Informasi lebih lanjut: <https://abrt.readthedocs.io/en/latest/usage.html>.

- Tampilkan daftar masalah yang terdeteksi:

`abrt-cli list`

- Tampilkan detail dari masalah tertentu:

`abrt-cli info {{problem_id}}`

- Hapus laporan crash:

`abrt-cli remove {{problem_id}}`

- Laporkan masalah ke bug tracker yang terkonfigurasi (misalnya Bugzilla):

`abrt-cli report {{problem_id}}`

- Pantau file log dan picu program saat kecocokan ditemukan:

`abrt-watch-log -F {{error_string}} {{/var/log/myapp.log}} {{notify-send "Crash detected"}}`

- Buat laporan untuk debugging secara manual:

`abrt-cli report {{[-a|--analyze]}} {{problem_id}}`
