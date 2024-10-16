# cal

> Tampilkan kalender dengan menyorot tanggal saat ini.
> Informasi lebih lanjut: <https://man.freebsd.org/cgi/man.cgi?cal>.

- Tampilkan kalender untuk bulan saat ini:

`cal`

- Tampilkan kalender untuk suatu tahun:

`cal {{tahun}}`

- Tampilkan kalender untuk suatu bulan dalam tahun:

`cal {{bulan}} {{tahun}}`

- Tampilkan seluruh kalender untuk tahun ini:

`cal -y`

- Jangan sorot ([h]ighlight) tanggal hari ini dan tampilkan kalender untuk [3] bulan yang mencakup tanggal tersebut:

`cal -h -3 {{bulan}} {{tahun}}`

- Tampilkan 2 bulan se[B]elum dan 3 setel[A]h bulan tertentu pada tahun berjalan:

`cal -A 3 -B 2 {{bulan}}`

- Tampilkan hari [j]ulian (hari sejak awal tahun, dimulai dengan nilai satu untuk 1 Januari):

`cal -j`
