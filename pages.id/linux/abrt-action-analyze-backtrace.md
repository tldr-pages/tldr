# abrt-action-analyze-backtrace

> Analisis backtrace C/C++.
> Hasilkan hash duplikasi, peringkat backtrace (backtrace rating), dan identifikasi fungsi crash.
> Simpan data sebagai elemen baru `duphash`, `rating`, `crash_function` di dalam direktori masalah.
> Informasi lebih lanjut: <https://manned.org/abrt-action-analyze-backtrace>.

- Lakukan analisis backtrace untuk direktori kerja (working directory) saat ini:

`abrt-action-analyze-backtrace`

- Lakukan analisis backtrace untuk direktori tertentu:

`abrt-action-analyze-backtrace -d {{path/ke/direktori}}`

- Lakukan analisis backtrace secara verbose:

`abrt-action-analyze-backtrace -v`
