# nice

> Jalankan suatu program dengan tingkatan prioritas penjadwalan secara kustom.
> Nilai prioritas (niceness) memili rentang antara -20 (prioritas terbesar) menuju 19 (terkecil).
> Catatan: Beberapa sistem penjadwalan modern mengabaikan nilai ini atau efeknya dalam kumpulan autogroup.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/nice-invocation.html>.

- Tampilkan nilai niceness saat ini:

`nice`

- Naikkan nilai niceness dengan 10:

`nice nice`

- Jalankan suatu program dengan prioritas rendah:

`nice -{{nilai_niceness}} {{perintah}}`

- Jalankan suatu program dengan prioritas tinggi:

`sudo nice --{{nilai_niceness}} {{perintah}}`

- Tentukan prioritas secara eksplisit:

`nice {{[-n|--adjustment]}} {{nilai_niceness}} {{perintah}}`
