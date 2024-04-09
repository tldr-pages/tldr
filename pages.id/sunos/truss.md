# truss

> Alat pemecah masalah untuk menelusuri panggilan sistem.
> strace untuk SunOS.
> Informasi lebih lanjut: <https://www.unix.com/man-page/linux/1/truss>.

- Telusuri sebuah program dengan mengeksekusinya dan mengawasi semua proses turunan:

`truss -f {{program}}`

- Mulai menelusuri sebuah proses tertentu berdasarkan PID-nya:

`truss -p {{pid}}`

- Mulai menelusuri sebuah program dengan mengeksekusinya, tampilkan argumen-argumen dan variabel-variabel lingkungan:

`truss -a -e {{program}}`

- Menghitung waktu, panggilan, dan error untuk setiap panggilan sistem dan laporkan sebuah ringkasan saat keluar program:

`truss -c -p {{pid}}`

- Telusuri proses berdasarkan keluaran dari panggilan sistem:

`truss -p {{pid}} -t {{nama_panggilan_sistem}}`
