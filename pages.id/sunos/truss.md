# truss

> Alat pemecah masalah untuk menelusuri panggilan sistem.
> strace untuk SunOS.
> Informasi lebih lanjut: <https://www.unix.com/man-page/linux/1/truss>.

- Mulai menelusuri sebuah program dengan mengeksekusinya, ikuti semua proses turunan:

`truss -f {{program}}`

- Mulai menelusuri sebuah proses tertentu berdasarkan PID-nya:

`truss -p {{pid}}`

- Mulia menelusuri sebuah program dengan mengeksekusinya, tampilkan argumen-argumen dan variabel-variabel lingkungan:

`truss -a -e {{program}}`

- Menghitung waktu, panggilan, dan error untuk setiap panggilan sistem dan laporkan sebuah ringkasan saat keluar program:

`truss -c -p {{pid}}`

- Trace a process filtering output by system call:

`truss -p {{pid}} -t {{system_call_name}}`
