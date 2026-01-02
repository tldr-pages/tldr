# tar

> Alat pengarsip berkas.
> Sering digunakan bersamaan dengan alat kompresi tertentu, seperti `gzip` atau `bzip2`.
> Informasi lebih lanjut: <https://www.gnu.org/software/tar/manual/tar.html>.

- Buat ([c]reate) suatu arsip dan simpan ke dalam suatu berkas ([f]ile):

`tar cf {{jalan/menuju/target.tar}} {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Buat ([c]reate) suatu arsip dengan tambahan kompresi g[z]ip dan simpan ke dalam suatu berkas ([f]ile):

`tar czf {{jalan/menuju/target.tar.gz}} {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Buat ([c]reate) suatu arsip dengan tambahan kompresi g[z]ip dari suatu direktori mengunakan alamat berkas relatif:

`tar czf {{jalan/menuju/target.tar.gz}} {{[-C|--directory]}} {{jalan/menuju/direktori}} .`

- E[x]trak suatu berkas ([f]ile) arsip (biasa atau terkompres) menuju direktori saat ini dengan menampilkan rincian operasi (mode [v]erbose):

`tar xvf {{jalan/menuju/sumber.tar[.gz|.bz2|.xz]}}`

- E[x]trak suatu berkas ([f]ile) arsip (biasa atau terkompres) menuju direktori target yang ditentukan:

`tar xf {{jalan/menuju/sumber.tar[.gz|.bz2|.xz]}} {{[-C|--directory]}} {{jalan/menuju/direktori}}`

- Buat ([c]reate) suatu arsip terkompres dan simpan di dalam suatu berkas ([f]ile), menggunakan metode kompresi yang ditentukan secara otom[a]tis berdasarkan nama ekstensi berkas tujuan:

`tar caf {{jalan/menuju/target.tar.xz}} {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- [t]ampilkan isi suatu berkas ([f]ile) tar secara rinci (mode [v]erbose):

`tar tvf {{jalan/menuju/sumber.tar}}`

- E[x]trak kumpulan berkas yang namanya memenuhi pola kriteria yang ditentukan dari suatu berkas ([f]ile) arsip:

`tar xf {{jalan/menuju/sumber.tar}} --wildcards "{{*.html}}"`
