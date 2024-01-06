# git bisect

> Lakukan strategi pencarian/pembelahan biner untuk mencari komit yang menyebabkan masalah/bug.
> Git akan secara otomatis melompat bolak-balik dalam grafik komit untuk semakin mempersempit kandidat komit yang bermasalah.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-bisect>.

- Jalankan sesi pembelahan biner pada suatu rentang komit antara komit bermasalah dan komit (biasanya terdahulu) yang diketahui tak bermasalah:

`git bisect start {{komit_bermasalah}} {{komit_baik}}`

- Untuk setiap komit yang dipilih oleh `git bisect`, tandai komit tersebut sebagai baik (good) atau buruk (bad) setelah mencobanya:

`git bisect {{good|bad}}`

- Setelah `git bisect` berhasil menemukan komit yang bermasalah, akhiri sesi pembelahan dan kembali kepada cabang sebelumnya:

`git bisect reset`

- Lewati pengecekan suatu komit saat proses pembelahan berlangsung (misal: karena terdapat masalah yang disebabkan oleh faktor lain):

`git bisect skip`

- Tampilkan log tentang kemajuan proses pembelahan saat ini:

`git bisect log`
